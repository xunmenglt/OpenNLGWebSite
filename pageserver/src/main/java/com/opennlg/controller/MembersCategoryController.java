package com.opennlg.controller;


import com.opennlg.pojo.MembersCategory;
import com.opennlg.service.IMembersCategoryService;
import com.opennlg.vo.RespBean;
import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * <p>
 * 成员类别 前端控制器
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@RestController
@RequestMapping("/members-category")
@Api(tags = "成员分类接口")
public class MembersCategoryController {
    @Autowired
    private IMembersCategoryService membersCategoryService;
    
    @GetMapping("/list")
    public RespBean getMembersCategoryList(){
        List<MembersCategory> categoryList= membersCategoryService.getMembersCategoryList();
        return RespBean.success("SUCCESS",categoryList);
    }
    
}
