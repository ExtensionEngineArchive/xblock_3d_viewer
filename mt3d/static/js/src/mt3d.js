/* Javascript for ModelViewer. */
function ModelViewer(runtime, element) {


  /*capturing html element where 3d model will be drawn*/
  var base =$('#cv',element).get(0);
  var viewer=new JSC3D.Viewer(base);

  /*handler for Ajax call*/
  var dFile=runtime.handlerUrl(element,'upload_objfile');
  /*collecting adress of model*/
  var model = $(".test" ,element).data("location-resouces");


  /*initialization of model viewer*/
   //viewer.setParameter('SceneUrl',dFile+"/?url="+model);
   viewer.setParameter('SceneUrl',model);
   viewer.setParameter('ModelColor', '#CAA618');
   viewer.setParameter('BackgroundColor1', $(".test").data("background"));
   viewer.setParameter('BackgroundColor2', $(".test").data("background1"));
   viewer.setParameter('RenderMode', 'texturesmooth');
   viewer.setParameter('Renderer', 'webgl');
   viewer.setParameter('MipMapping','on');
   viewer.setParameter('ProgressBar','off');
   viewer.init();
   viewer.update();

}
