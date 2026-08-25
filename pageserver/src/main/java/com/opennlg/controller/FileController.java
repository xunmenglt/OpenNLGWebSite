package com.opennlg.controller;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.opennlg.vo.RespBean;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
 
/**
 * description: 文件上传Controller
 * @version v1.0
 * @author w
 * @date 2021年3月16日上午11:19:34
 **/
@RestController
@RequestMapping("/file")
@Api(tags = "文件操作接口")
public class FileController {
 
	/**
	 *  上传文件目录
	 */
	@Value(value = "${file.path}")
	private String userfileDir ;

	@Value(value = "${file.domain}")
	private String domain ;

	@ApiOperation("上传单个文件")
	@PostMapping(value = "/upload")
	public RespBean upload(MultipartFile file){
		if(null == file) {
			return RespBean.fail("文件不能为空");
		}
		String originalFilename = file.getOriginalFilename();
		File dest = new File(userfileDir);
		if(!dest.exists() && !dest.isDirectory()) {
			dest.mkdirs();
		}
		try {
			file.transferTo(new File(dest , originalFilename));
		} catch (IllegalStateException | IOException e) {
			e.printStackTrace();
			return RespBean.fail("文件上传失败") ;
		}
		String url=domain.concat(originalFilename);
		return RespBean.success("上传成功",url);
	}

	@ApiOperation("上传多个文件")
	@PostMapping(value = "/uploads")
	public RespBean uploads(MultipartFile files[]){
		Map<String, Object> map = new HashMap<String, Object>();
		if(null == files || files.length == 0) {
			return RespBean.fail("上传文件不能为空");
		}

		List<String> list = new ArrayList<String>();

		for (MultipartFile file : files) {
			String originalFilename = file.getOriginalFilename();
			File dest = new File(userfileDir);
			if(!dest.exists() && !dest.isDirectory()) {
				dest.mkdirs();
			}
			try {
				file.transferTo(new File(dest , originalFilename));
			} catch (IllegalStateException | IOException e) {
				e.printStackTrace();
				return RespBean.fail("上传失败");
			}
			list.add(originalFilename);
		}
		List<String> urlList = list.stream().map((e) -> domain.concat(e)).collect(Collectors.toList());

		return RespBean.success("上传成功",urlList);
	}
}