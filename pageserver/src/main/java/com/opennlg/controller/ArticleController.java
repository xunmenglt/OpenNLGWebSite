package com.opennlg.controller;


import com.opennlg.pojo.Article;
import com.opennlg.service.IArticleService;
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
@RequestMapping("/article")
@Api(tags = "文章操作接口")
public class ArticleController {
    @Autowired
    private IArticleService articleService;


    @ApiOperation("创建文章")
    @PostMapping("/create")
    public RespBean createArticle(@RequestBody Article article){
        return articleService.createArticle(article);
    }


    @ApiOperation("删除文章")
    @PostMapping("/delete/{id}")
    public RespBean deleteArticle(@PathVariable(value = "id") String id){
        return articleService.deleteArticle(id);
    }


    @ApiOperation("修改文章")
    @PostMapping("/update")
    public RespBean updateArticle(@RequestBody Article article){
        return articleService.updateArticle(article);
    }


    @ApiOperation("获取文章")
    @GetMapping("/item")
    public RespBean itemArticle(@RequestParam(value = "articleId",required = true) String articleId){
        return articleService.getArticle(articleId);
    }
    @ApiOperation("获取文章列表")
    @GetMapping("/list")
    public RespBean listArticle(@RequestParam(value = "currentPage",defaultValue = "1") Integer currentPage,
                             @RequestParam(value = "size",defaultValue = "10") Integer size){
        return articleService.getArticleList(currentPage,size);
    }
}
