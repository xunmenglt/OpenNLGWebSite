package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import java.time.LocalDateTime;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;

import com.fasterxml.jackson.annotation.JsonFormat;
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
 * @since 2023-11-02
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_reserarch")
@ApiModel(value="Reserarch对象", description="")
public class Reserarch implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "研究文章id")
    @TableId(value = "reserarch_id", type = IdType.AUTO)
    private Integer reserarchId;

    @ApiModelProperty(value = "研究文章标题")
    @TableField("reserarch_title")
    private String reserarchTitle;

    @ApiModelProperty(value = "研究文章来源")
    @TableField("reserarch_source")
    private String reserarchSource;

    @ApiModelProperty(value = "研究文章作者")
    @TableField("reserarch_author")
    private String reserarchAuthor;

    @ApiModelProperty(value = "正式发表年份")
    @TableField("publication_year")
    private Integer publicationYear;

    @ApiModelProperty(value = "论文类型")
    @TableField("publication_type")
    private String publicationType;

    @ApiModelProperty(value = "研究方向")
    @TableField("research_direction")
    private String researchDirection;

    @ApiModelProperty(value = "会议或期刊简称")
    @TableField("venue_short_name")
    private String venueShortName;

    @ApiModelProperty(value = "PDF链接")
    @TableField("pdf_url")
    private String pdfUrl;

    @ApiModelProperty(value = "DOI链接")
    @TableField("doi_url")
    private String doiUrl;

    @ApiModelProperty(value = "代码链接")
    @TableField("code_url")
    private String codeUrl;

    @ApiModelProperty(value = "项目链接")
    @TableField("project_url")
    private String projectUrl;

    @ApiModelProperty(value = "研究文章封面")
    @TableField("reserarch_cover")
    private String reserarchCover;

    @ApiModelProperty(value = "是否是最新发布")
    @TableField("is_new")
    private Integer isNew;

    @ApiModelProperty(value = "外链")
    @TableField("outside_url")
    private String outsideUrl;

    @ApiModelProperty(value = "内链")
    @TableField("inside_url")
    private String insideUrl;

    @ApiModelProperty(value = "创建时间")
    @TableField("create_time")
    @JsonFormat(pattern="yyyy-MM-dd",timezone="GMT+8")
    @JsonDeserialize(using = CustomTimeDeserializer.class)
    private LocalDateTime createTime;

    @ApiModelProperty(value = "更新时间")
    @TableField("update_time")
    @JsonFormat(pattern="yyyy-MM-dd",timezone="GMT+8")
    @JsonDeserialize(using = CustomTimeDeserializer.class)
    private LocalDateTime updateTime;


}
