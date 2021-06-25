package com.fantasy.kvdatabase.db;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.util.Map;

public class HashIdxKvDBDBTest {
    private HashIdxKvDB hashIdxKvDB;

    @Before
    public void createBD() throws IOException {
        String path = "D:\\IdeaProjects\\KVDatabase\\src\\database.log";
        String idxPath = "D:\\IdeaProjects\\KVDatabase\\src\\database.idx";
        hashIdxKvDB = new HashIdxKvDB(path, idxPath);
    }

    @Test
    public void testGetIdx() throws IOException {
        Map<String, Long> result = hashIdxKvDB.getIdx();
        Assert.assertTrue(result.size()==10);
        hashIdxKvDB.set("10","10");
        Assert.assertTrue(result.size()==11);
    }

    @Test
    public void testSet() throws IOException {

        for (int i = 0; i < 10; ++i) {
            hashIdxKvDB.set(String.valueOf(i), String.valueOf(i + 1));
        }
        Assert.assertEquals(10, hashIdxKvDB.getIdx().size());
        Assert.assertEquals("1", hashIdxKvDB.get("0"));
        Assert.assertEquals("10", hashIdxKvDB.get("9"));

    }

    @Test
    public void testGet() throws IOException {
        for (int i = 0; i < 10; ++i) {
            hashIdxKvDB.set(String.valueOf(i), String.valueOf(i + 1));
        }
        String result;
        result=hashIdxKvDB.get(String.valueOf(1));
        Assert.assertEquals("2", result);

//        System.out.println(hashIdxKvDB.get(String.valueOf(1)));
        result=hashIdxKvDB.get(String.valueOf(8));
        Assert.assertEquals("9", result);

//        System.out.println(hashIdxKvDB.get(String.valueOf(8)));
        result=hashIdxKvDB.get(String.valueOf(20));
        Assert.assertEquals("", result);

//        System.out.println(hashIdxKvDB.get(String.valueOf(20)));
    }


    @After
    public void closeDB() throws IOException {
        hashIdxKvDB.close();
    }
}
