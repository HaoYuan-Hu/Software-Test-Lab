package com.fantasy.kvdatabase.db;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;

public class CompactionHashIdxKvDBTest {
    private CompactionHashIdxKvDB compactionHashIdxKvDB;

    @Before
    public void createBD() {
        compactionHashIdxKvDB = new CompactionHashIdxKvDB();
    }

    @Test
    public void testCurrent() throws IOException {
        compactionHashIdxKvDB.set(String.valueOf(10), String.valueOf(11));
        String result = compactionHashIdxKvDB.get(String.valueOf(10));
        Assert.assertEquals(result,String.valueOf(11));

        for(int i=11;i<15;++i){
            compactionHashIdxKvDB.set(String.valueOf(i), String.valueOf(i+1));
        }
        result = compactionHashIdxKvDB.get(String.valueOf(10));
        Assert.assertEquals(result,String.valueOf(11));
    }

    @After
    public void closeDB() {
        compactionHashIdxKvDB.close();
    }
}
