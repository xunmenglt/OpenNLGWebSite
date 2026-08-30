package com.opennlg.mapper;

import com.opennlg.pojo.Members;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.opennlg.pojo.MembersCategory;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface MembersMapper extends BaseMapper<Members> {

    List<MembersCategory> selectMembersList();

    Members selectMemberAdminItem(@Param("memberId") Integer memberId);

    void hideMemberRelations(@Param("memberId") Integer memberId);

    void upsertPrimaryMemberRelation(@Param("memberId") Integer memberId,
                                     @Param("ctType") String ctType,
                                     @Param("serialNum") Integer serialNum);

    void deleteMemberEducation(@Param("memberId") Integer memberId,
                               @Param("degreeType") String degreeType);

    void insertMemberEducation(@Param("memberId") Integer memberId,
                               @Param("degreeType") String degreeType,
                               @Param("cohortYear") Integer cohortYear,
                               @Param("cohortLabel") String cohortLabel,
                               @Param("programType") String programType,
                               @Param("graduationDestination") String graduationDestination,
                               @Param("displayOrder") Integer displayOrder);
    
}
