package com.opennlg.controller;


import com.opennlg.pojo.Members;
import com.opennlg.service.IMembersService;
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
@RequestMapping("/members")
@Api(tags = "实验室成员操作接口")
public class MembersController {
    @Autowired
    private IMembersService membersService;
    
    @ApiOperation("创建成员")
    @PostMapping("/create")
    public RespBean createMembers(@RequestBody Members members){
        return membersService.createMembers(members);
    }


    @ApiOperation("删除成员")
    @PostMapping("/delete/{id}")
    public RespBean deleteMembers(@PathVariable(value = "id") Integer id){
        return membersService.deleteMembers(id);
    }


    @ApiOperation("修改成员")
    @PostMapping("/update")
    public RespBean updateMembers(@RequestBody Members members){
        return membersService.updateMembers(members);
    }


    @ApiOperation("获取成员列表")
    @GetMapping("/list")
    public RespBean listMembers(){
        return membersService.getMembersList();
    }

    @ApiOperation("获取成员列表")
    @GetMapping("/coverlist")
    public RespBean coverListMembers(){
        return membersService.getCoverMembersList();
    }

    @ApiOperation("获取成员")
    @GetMapping("/item")
    public RespBean itemMembers(@RequestParam(value = "membersId",required = true) Integer membersId){
        return membersService.getMembers(membersId);
    }
}
