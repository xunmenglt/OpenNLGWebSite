package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import java.time.LocalDateTime;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 * 
 * </p>
 *
 * @author Liuteng
 * @since 2023-10-31
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_article")
@ApiModel(value="Article对象", description="")
public class Article implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "id")
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @ApiModelProperty(value = "文章id")
    @TableField("article_id")
    private String articleId;

    @ApiModelProperty(value = "文章标题")
    @TableField("article_title")
    private String articleTitle;

    @ApiModelProperty(value = "文章概要")
    @TableField("article_summary")
    private String articleSummary;

    @ApiModelProperty(value = "文章内容")
    @TableField("article_content")
    private String articleContent;

    @ApiModelProperty(value = "文章阅读次数")
    @TableField("article_read_times")
    private Integer articleReadTimes;

    @ApiModelProperty(value = "创建时间")
    @TableField("create_time")
    @JsonFormat(pattern="yyyy-MM-dd HH:ss:mm",timezone="GMT+8")
    private LocalDateTime createTime;

    @ApiModelProperty(value = "更新时间")
    @TableField("update_time")
    @JsonIgnore
    private LocalDateTime updateTime;


}
