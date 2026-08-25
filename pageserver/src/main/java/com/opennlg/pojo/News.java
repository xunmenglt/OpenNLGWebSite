package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import java.time.LocalDateTime;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.opennlg.config.deserializer.CustomTimeDeserializer;
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
@TableName("og_news")
@ApiModel(value="News对象", description="")
public class News implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "新闻id")
    @TableId(value = "news_id", type = IdType.AUTO)
    private Integer newsId;

    @ApiModelProperty(value = "新闻标题")
    @TableField("news_title")
    private String newsTitle;

    @ApiModelProperty(value = "新闻概要")
    @TableField("news_summary")
    private String newsSummary;

    @ApiModelProperty(value = "阅读次数")
    @TableField("news_read_times")
    private Integer newsReadTimes;

    @ApiModelProperty(value = "外链路径")
    @TableField("outside_url")
    private String outsideUrl;

    @ApiModelProperty(value = "内链路径")
    @TableField("inside_url")
    private String insideUrl;

    @ApiModelProperty(value = "创建时间")
    @TableField("create_time")
    @JsonFormat(pattern="yyyy/MM/dd",timezone="GMT+8")
    @JsonDeserialize(using = CustomTimeDeserializer.class)
    private LocalDateTime createTime;

    @ApiModelProperty(value = "更新时间")
    @TableField("update_time")
    @JsonIgnore
    private LocalDateTime updateTime;

    @ApiModelProperty(value = "是否是新的")
    @TableField("is_new")
    private Integer isNew;


}
