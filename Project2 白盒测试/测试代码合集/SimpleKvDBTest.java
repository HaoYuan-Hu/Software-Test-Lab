package com.fantasy.kvdatabase.db;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import java.io.IOException;

public class SimpleKvDBTest {
    private SimpleKvDB simpleKvDB;

    @Before
    public void createBD() {
        String path = "D:\\IdeaProjects\\KVDatabase\\src\\database.data";
        simpleKvDB = new SimpleKvDB(path);
    }

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Test
    public void testGet() throws IOException {
//        System.out.println(simpleKvDB.get(String.valueOf(1)));
//        System.out.println(simpleKvDB.get(String.valueOf(20)));
          try{simpleKvDB.get(String.valueOf(0));}
          catch (IndexOutOfBoundsException anIndexOutOfBoundsException){
              thrown.expect(IndexOutOfBoundsException.class);
          }
          simpleKvDB.set(String.valueOf(0),String.valueOf(1));
          String result = simpleKvDB.get(String.valueOf(0));
          Assert.assertEquals("1",result);
    }

    @Test
    public void testSet() throws IOException {
        for (int i = 1; i < 20; ++i) {
            simpleKvDB.set(String.valueOf(i), String.valueOf(i + 1));
        }
    }
}
