package com.opennlg.service;

import com.opennlg.pojo.MembersCategory;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 * 成员类别 服务类
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
public interface IMembersCategoryService extends IService<MembersCategory> {

    List<MembersCategory> getMembersCategoryList();
}
