package com.opennlg;

import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class Test {
    @Autowired
    private PasswordEncoder passwordEncoder;
    @org.junit.Test
    public void generatePassword(){
        String password="88888888";
        String ciphertext = passwordEncoder.encode(password);
        System.out.println(ciphertext);
    }
}
