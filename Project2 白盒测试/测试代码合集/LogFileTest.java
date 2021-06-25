package com.fantasy.kvdatabase.logfile;


import com.fantasy.kvdatabase.util.Constant;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.Assert;
import org.junit.rules.ExpectedException;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.internal.matchers.GreaterThan;


import javax.persistence.criteria.CriteriaBuilder;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

import static org.mockito.Matchers.anyInt;
import static org.mockito.Matchers.anyString;
import static org.mockito.Mockito.*;


public class LogFileTest {
//    @Mock
    private  LogFile logFile;


    @Before
    public void setUp(){
        String path = Constant.DATA_FILE_URL;
//        MockitoAnnotations.initMocks(this);
//        doCallRealMethod().when(logFile).create(anyString());
        logFile=LogFile.create(path+"try");
        Assert.assertNotNull(logFile);
    }

    @Test
    public void create() {

    }

    @Test
    public void append() throws IOException {
        Long ret=logFile.append("123");
        Assert.assertNotEquals(java.util.Optional.of(0L),ret);
   }

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Test
    public void read() throws IOException {
        try{logFile.read(-1);}
        catch (IndexOutOfBoundsException anIndexOutOfBoundsException){
            thrown.expect(IndexOutOfBoundsException.class);
        }
        Long ret=logFile.append("123");
        String result=logFile.read(ret);
        Assert.assertEquals("123",result);
    }

    @Test
    public void lines() throws IOException {
        Stream<String> result= logFile.lines();
        Assert.assertNotNull(result);
    }

    @Test
    public void size() {
        long result=logFile.size();
        Assert.assertTrue(result>0);
    }

    @Test
    public void path() {
        String result=logFile.path();
        Assert.assertEquals(Constant.DATA_FILE_URL+"try",result);
        System.out.println(result);
    }

    @Test
    public void renameTo() {
        logFile.renameTo(Constant.DATA_FILE_URL+"another");
        String result=logFile.path();
        Assert.assertEquals(Constant.DATA_FILE_URL+"another",result);
        System.out.println(result);
    }

    @Test
    public void delete() throws IOException {
        logFile.delete();
        Files.createFile(logFile.getIdxPath());
//        verify(logFile,times(1)).delete();
    }

    @Test
    public void getDataPath() {
        Path result = logFile.getDataPath();
        String origin=logFile.path();
        Assert.assertEquals(origin+".data",result.toString());
    }

    @Test
    public void getIdxPath() {
        Path result = logFile.getIdxPath();
        String origin=logFile.path();
        Assert.assertEquals(origin+".idx",result.toString());
    }

    @Test
    public void testToString() {
        String result = logFile.toString();
        System.out.println(result);
        Assert.assertEquals(result,"LogFile{dataPath=D:\\IdeaProjects\\KVDatabase\\data\\logtry.data, idxPath=D:\\IdeaProjects\\KVDatabase\\data\\logtry.idx}");
    }
}
