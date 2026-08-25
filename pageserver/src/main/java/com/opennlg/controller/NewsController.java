package com.opennlg.controller;


import com.opennlg.pojo.News;
import com.opennlg.service.INewsService;
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
 * @since 2023-10-31
 */
@RestController
@RequestMapping("/news")
@Api(tags = "实验室新闻操作接口")
public class NewsController {


    @Autowired
    private INewsService newsService;


    @ApiOperation("创建新闻")
    @PostMapping("/create")
    public RespBean createNews(@RequestBody News news){
        return newsService.createNews(news);
    }


    @ApiOperation("删除新闻")
    @PostMapping("/delete/{id}")
    public RespBean deleteNews(@PathVariable(value = "id") Integer id){
        return newsService.deleteNews(id);
    }


    @ApiOperation("修改新闻")
    @PostMapping("/update")
    public RespBean updateNews(@RequestBody News news){
        return newsService.updateNews(news);
    }


    @ApiOperation("获取新闻列表")
    @GetMapping("/list")
    public RespBean listNews(@RequestParam(value = "currentPage",defaultValue = "1") Integer currentPage,
                             @RequestParam(value = "size",defaultValue = "10") Integer size){
        return newsService.getNewsList(currentPage,size);
    }

    @ApiOperation("获取新闻")
    @GetMapping("/item")
    public RespBean itemNews(@RequestParam(value = "newsId",required = true) Integer newsId){
        return newsService.getNews(newsId);
    }
}
