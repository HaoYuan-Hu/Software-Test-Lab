private void compactLevel2() throws IOException {
    System.out.println("进行Level2 Compact!!!");
    // 生成一份快照
    Deque<LogFile> snapshot = new LinkedList<>(compactedLevel1);
    if (snapshot.isEmpty()) {
        return;
    }

    int compactSize = snapshot.size();
    // level2的文件命名规则为：filename_level2_num
    LogFile newLogFile = LogFile.create(curLog.path() + "_level2_" + level2Num.getAndIncrement());
    while (!snapshot.isEmpty()) {
        // 从最新的level1 compacted segment file开始处理
        LogFile logFile = snapshot.pollLast();
        idx.allIdxOf(logFile).forEach((key, offset) -> {
            if (idx.idxOf(newLogFile, key) == -1) {
                final String record = logFile.read(offset);
                idx.addIdx(newLogFile, key, newLogFile.append(record));
            }
        });
    }

    compactedLevel2.addLast(newLogFile);
    // 写入完成后，删除compactedLevel1队列中相应的文件
    while (compactSize > 0) {
        LogFile logFile = compactedLevel1.pollFirst();
        deleteLogFile(logFile);
        --compactSize;
    }
}