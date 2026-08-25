package com.opennlg.config.security.pojo;

import com.opennlg.pojo.User;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Component
public class LoginUser implements UserDetails, Serializable {
    private static final long serialVersionUID = 1L;


    private User user;

//
    private List<String> roles;

    public LoginUser(User user){
        this.user=user;
        List<String> _roles=new ArrayList<>();
        _roles.add("ADMIN");
        this.roles=_roles;
    }

    private List<SimpleGrantedAuthority> authorities;

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {

        List<SimpleGrantedAuthority> authorityList=new ArrayList<>();

        for (String  role: roles) {
            SimpleGrantedAuthority simpleGrantedAuthority=new SimpleGrantedAuthority(role);
            authorityList.add(simpleGrantedAuthority);
        }

        return authorityList;
    }


    @Override
    public String getPassword() {
        return user.getPassword();
    }

    @Override
    public String getUsername() {
        return user.getUsername();
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
