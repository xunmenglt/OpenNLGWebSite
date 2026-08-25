package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import java.time.LocalDateTime;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;

import com.fasterxml.jackson.annotation.JsonFormat;
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
 * @since 2023-11-02
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_publication")
@ApiModel(value="Publication对象", description="")
public class Publication implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "项目id")
    @TableId(value = "publication_id", type = IdType.AUTO)
    private Integer publicationId;

    @ApiModelProperty(value = "项目标题")
    @TableField("publication_title")
    private String publicationTitle;

    @ApiModelProperty(value = "项目名称")
    @TableField("publication_desc")
    private String publicationDesc;

    @ApiModelProperty(value = "项目封面")
    @TableField("publication_cover")
    private String publicationCover;

    @ApiModelProperty(value = "外链")
    @TableField("outside_url")
    private String outsideUrl;

    @ApiModelProperty(value = "内链")
    @TableField("inside_url")
    private String insideUrl;

    @ApiModelProperty(value = "创建时间")
    @TableField("create_time")
    @JsonFormat(pattern="yyyy-MM-dd HH:ss:mm",timezone="GMT+8")
    private LocalDateTime createTime;

    @ApiModelProperty(value = "更新时间")
    @TableField("update_time")
    @JsonFormat(pattern="yyyy-MM-dd HH:ss:mm",timezone="GMT+8")
    private LocalDateTime updateTime;


}
