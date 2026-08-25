package com.opennlg.config.security;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opennlg.vo.RespBean;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.web.access.AccessDeniedHandler;
import org.springframework.stereotype.Component;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@Component
public class AccessDeniedHandlerImpl implements AccessDeniedHandler {
    @Override
    public void handle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, AccessDeniedException e) throws IOException, ServletException {
        httpServletResponse.setCharacterEncoding("UTF-8");
        httpServletResponse.setContentType("application/json");
        httpServletResponse.setStatus(403);
        PrintWriter writer = httpServletResponse.getWriter();
        writer.write(new ObjectMapper().writeValueAsString(new RespBean(403, e.getMessage(), null)));
        writer.flush();
        writer.close();
    }
}
