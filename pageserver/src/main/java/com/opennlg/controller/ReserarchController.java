package com.opennlg.controller;


import com.opennlg.pojo.Reserarch;
import com.opennlg.service.IReserarchService;
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
@RequestMapping("/reserarch")
@Api(tags = "研究文章操作接口")
public class ReserarchController {
    @Autowired
    private IReserarchService reserarchService;


    @ApiOperation("创建论文")
    @PostMapping("/create")
    public RespBean createReserarch(@RequestBody Reserarch reserarch){
        return reserarchService.createReserarch(reserarch);
    }


    @ApiOperation("删除论文")
    @PostMapping("/delete/{id}")
    public RespBean deleteReserarch(@PathVariable(value = "id") Integer id){
        return reserarchService.deleteReserarch(id);
    }


    @ApiOperation("修改论文")
    @PostMapping("/update")
    public RespBean updateReserarch(@RequestBody Reserarch reserarch){
        return reserarchService.updateReserarch(reserarch);
    }


    @ApiOperation("获取论文列表")
    @GetMapping("/list")
    public RespBean listReserarch(@RequestParam(value = "currentPage",defaultValue = "1") Integer currentPage,
                             @RequestParam(value = "size",defaultValue = "10") Integer size){
        return reserarchService.getReserarchList(currentPage,size);
    }

    @ApiOperation("获取论文")
    @GetMapping("/item")
    public RespBean itemReserarch(@RequestParam(value = "reserarchId",required = true) Integer reserarchId){
        return reserarchService.getReserarch(reserarchId);
    }
}
