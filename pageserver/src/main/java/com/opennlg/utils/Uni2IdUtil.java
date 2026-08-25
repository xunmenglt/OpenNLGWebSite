package com.opennlg.utils;

import cn.hutool.core.util.RandomUtil;

abstract public class Uni2IdUtil {
    private static final String articleIdPrefix="article_";
    public static String createArticleId(){
        return articleIdPrefix+ RandomUtil.randomNumbers(20-articleIdPrefix.length());
    }
}

