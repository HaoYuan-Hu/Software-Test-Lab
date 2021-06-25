private void loadIdx() {
    // 获取目录下所有文件
    final File[] files = new File(Constant.DATA_FILE_PREFIX).listFiles();
    if (files != null && files.length > 0) {
        // 先排序
        Arrays.sort(files, Comparator.comparing(File::getName));

        Arrays.stream(files).forEach(file -> {
            try {
                if (file.getAbsolutePath().endsWith(".data")) {
                    final String fileName = Util.getFileName(file.getAbsolutePath());
                    LogFile logFile = new LogFile(fileName);

                    if (new File(fileName + Constant.IDX_FILE_SUFFIX).exists()) {
                        Files.lines(Paths.get(fileName + Constant.IDX_FILE_SUFFIX)).forEach(x -> {
                            final Pair<String, Long> pair = Util.decomposeIdx(x);
                            idx.addIdx(logFile, pair.getKey(), pair.getValue());
                        });
                    }

                    if (fileName.contains("_level1_")) {
                        compactedLevel1.addLast(logFile);
                        level1Num = new AtomicInteger(
                                Math.max(level1Num.get(),
                                        Integer.parseInt(fileName.substring(fileName.indexOf("_level1_") + "_level1_".length()))));
                    } else if (fileName.contains("_level2_")) {
                        compactedLevel2.addLast(logFile);
                        level2Num = new AtomicInteger(
                                Math.max(level2Num.get(),
                                        Integer.parseInt(fileName.substring(fileName.indexOf("_level2_") + "_level2_".length()))));
                    } else if (fileName.contains("_")) {
                        toCompact.addLast(logFile);
                        toCompactNum = new AtomicInteger(
                                Math.max(toCompactNum.get(),
                                        Integer.parseInt(fileName.substring(fileName.indexOf("_") + "_".length()))));
                    } else {
                        curLog = logFile;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
    }

    if (curLog == null) {
        curLog = new LogFile(Constant.DATA_FILE_URL);
    }
}
