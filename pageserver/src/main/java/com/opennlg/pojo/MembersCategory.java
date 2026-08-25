package com.opennlg.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;
import java.util.List;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 * 成员类别
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("og_members_category")
@ApiModel(value="MembersCategory对象", description="成员类别")
public class MembersCategory implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "类别")
    @TableId("ct_type")
    private String ctType;

    @ApiModelProperty(value = "类别中文名称")
    @TableField("ct_zh_name")
    private String ctZhName;

    @ApiModelProperty(value = "排序")
    private Integer sort;
    
    @ApiModelProperty(value = "团队成员")
    @TableField(exist = false)
    private List<Members> children;


}
