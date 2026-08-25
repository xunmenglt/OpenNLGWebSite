package com.opennlg.vo;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * 分页之后的结果
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class RespPageBean {
    //当前页
    private Long currentPage;

    //当前页面大小
    private Long size;

    //总记录数量
    private Long total;

    //数据
    private List<?> data;


    //封装pageBean函数
    public static RespPageBean tranPageBeanByPageObject(Page page){
        //封装respage对象
        RespPageBean pageBean=new RespPageBean();
        pageBean.setCurrentPage(page.getCurrent());
        pageBean.setSize(page.getSize());
        pageBean.setTotal(page.getTotal());
        pageBean.setData(page.getRecords());
        return pageBean;
    }
}