package com.opennlg.controller;


import com.opennlg.pojo.Publication;
import com.opennlg.service.IPublicationService;
import com.opennlg.vo.RespBean;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
@RestController
@RequestMapping("/publication")
@Api(tags = "项目操作接口")
public class PublicationController {
    @Autowired
    private IPublicationService publicationService;


    @ApiOperation("创建项目")
    @PostMapping("/create")
    public RespBean createPublication(@RequestBody Publication publication){
        return publicationService.createPublication(publication);
    }


    @ApiOperation("删除项目")
    @PostMapping("/delete/{id}")
    public RespBean deletePublication(@PathVariable(value = "id") Integer id){
        return publicationService.deletePublication(id);
    }


    @ApiOperation("修改项目")
    @PostMapping("/update")
    public RespBean updatePublication(@RequestBody Publication publication){
        return publicationService.updatePublication(publication);
    }


    @ApiOperation("获取项目列表")
    @GetMapping("/list")
    public RespBean listPublication(@RequestParam(value = "currentPage",defaultValue = "1") Integer currentPage,
                             @RequestParam(value = "size",defaultValue = "10") Integer size){
        return publicationService.getPublicationList(currentPage,size);
    }

    @ApiOperation("获取项目")
    @GetMapping("/item")
    public RespBean itemPublication(@RequestParam(value = "publicationId",required = true) Integer publicationId){
        return publicationService.getPublication(publicationId);
    }
}
