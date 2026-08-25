package com.opennlg.config.cache;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

abstract public class SecurityCache {
    public static final ConcurrentMap<String,Object> container=new ConcurrentHashMap<>();
}
