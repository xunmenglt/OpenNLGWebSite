package com.opennlg.config.deserializer;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import org.springframework.util.ObjectUtils;

import java.io.IOException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class CustomTimeDeserializer extends JsonDeserializer<LocalDateTime> {
    @Override
    public LocalDateTime deserialize(JsonParser jsonParser, DeserializationContext deserializationContext) throws IOException, JsonProcessingException {

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        String dateStr = jsonParser.getText();
        if (ObjectUtils.isEmpty(dateStr)){
            return null;
        }

        LocalDateTime localDateTime=null;
        try {
            LocalDate localDate = LocalDate.parse(dateStr, fmt);
            localDateTime=localDate.atStartOfDay();
        }catch (Exception e){
            return null;
        }
        return localDateTime;
    }
}
