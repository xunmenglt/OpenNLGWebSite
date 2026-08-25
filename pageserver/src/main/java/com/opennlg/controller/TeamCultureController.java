package com.opennlg.controller;


import com.opennlg.pojo.TeamCulture;
import com.opennlg.service.ITeamCultureService;
import com.opennlg.vo.RespBean;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>
 * 团队文化 前端控制器
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@RestController
@RequestMapping("/team-culture")
@Api(tags = "团队文化管理")
public class TeamCultureController {
    @Autowired
    private ITeamCultureService teamCultureService;


    @ApiOperation("创建文化")
    @PostMapping("/create")
    public RespBean createTeamCulture(@RequestBody TeamCulture reserarch){
        return teamCultureService.createTeamCulture(reserarch);
    }


    @ApiOperation("删除文化")
    @PostMapping("/delete/{id}")
    public RespBean deleteTeamCulture(@PathVariable(value = "id") Integer id){
        return teamCultureService.deleteTeamCulture(id);
    }


    @ApiOperation("修改文化")
    @PostMapping("/update")
    public RespBean updateTeamCulture(@RequestBody TeamCulture reserarch){
        return teamCultureService.updateTeamCulture(reserarch);
    }


    @ApiOperation("获取文化列表")
    @GetMapping("/list")
    public RespBean listTeamCulture(@RequestParam(value = "currentPage",defaultValue = "1") Integer currentPage,
                                  @RequestParam(value = "size",defaultValue = "10") Integer size){
        return teamCultureService.getTeamCultureList(currentPage,size);
    }

    @ApiOperation("获取文化")
    @GetMapping("/item")
    public RespBean itemTeamCulture(@RequestParam(value = "reserarchId",required = true) Integer reserarchId){
        return teamCultureService.getTeamCulture(reserarchId);
    }
}
