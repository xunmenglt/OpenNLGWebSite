package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;
import java.time.LocalDateTime;

import com.fasterxml.jackson.annotation.JsonFormat;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 * 团队文化
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_team_culture")
@ApiModel(value="TeamCulture对象", description="团队文化")
public class TeamCulture implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "唯一id")
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @ApiModelProperty(value = "图像")
    private String image;

    @ApiModelProperty(value = "标题")
    private String title;

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

}
