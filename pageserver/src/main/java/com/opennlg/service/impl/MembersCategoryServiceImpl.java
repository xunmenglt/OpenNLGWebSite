package com.opennlg.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.opennlg.pojo.MembersCategory;
import com.opennlg.mapper.MembersCategoryMapper;
import com.opennlg.service.IMembersCategoryService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * <p>
 * 成员类别 服务实现类
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@Service
public class MembersCategoryServiceImpl extends ServiceImpl<MembersCategoryMapper, MembersCategory> implements IMembersCategoryService {
    @Autowired
    private MembersCategoryMapper membersCategoryMapper;
    @Override
    public List<MembersCategory> getMembersCategoryList() {
        List<MembersCategory> categoryList = membersCategoryMapper.selectList(new QueryWrapper<MembersCategory>().orderByAsc("sort"));
        return categoryList;
    }
}
