/**
* 上传文件，需要点击弹出上传照片的窗口才行
*
* @parambrower
*            使用的浏览器名称
* @paramfile
*            需要上传的文件及文件名
*/
# 先去用selenium点击上传文件按钮，
# 之后会弹出上传文件输入框，
# 最后执行上面那个public void handleUpload(String browser, File file)方法即可。
publicvoidhandleUpload(String browser, File file) {
    String filePath= file.getAbsolutePath();
    String executeFile= "res/script/autoit/Upload.exe"; //定义了upload.exe文件的路径
    String cmd= "\""+ executeFile+ "\""+ " "+ "\""+ browser+ "\""+ " "+ "\""+ filePath+ "\"";
    try{
        Process p= Runtime.getRuntime().exec(cmd);
        p.waitFor();
    } catch(Exception e) {
        e.printStackTrace();
    }
}