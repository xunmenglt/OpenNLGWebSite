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
 * @since 2023-11-02
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_members")
@ApiModel(value="Members对象", description="")
public class Members implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "成员id")
    @TableId(value = "member_id", type = IdType.AUTO)
    private Integer memberId;

    @ApiModelProperty(value = "中文名称")
    @TableField("cn_name")
    private String cnName;

    @ApiModelProperty(value = "英文名称")
    @TableField("en_name")
    private String enName;

    @ApiModelProperty(value = "描述")
    private String memberDesc;

    @ApiModelProperty(value = "职业")
    private String profession;

    @ApiModelProperty(value = "方向")
    private String direction;

    @ApiModelProperty(value = "邮箱")
    private String email;

    @ApiModelProperty(value = "类别")
    private String ctType;

    @ApiModelProperty(value = "序号")
    @TableField("serial_num")
    private Integer serialNum;

    @ApiModelProperty(value = "头像链接")
    @TableField("avatar_url")
    private String avatarUrl;

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

    @ApiModelProperty(value = "登记年级")
    @TableField(exist = false)
    private Integer cohortYear;

    @ApiModelProperty(value = "原始年级标签")
    @TableField(exist = false)
    private String cohortLabel;

    @ApiModelProperty(value = "培养类型")
    @TableField(exist = false)
    private String programType;

    @ApiModelProperty(value = "学历")
    @TableField(exist = false)
    private String degreeType;

    @ApiModelProperty(value = "毕业去向")
    @TableField(exist = false)
    private String graduationDestination;


}
