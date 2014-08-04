"""Mt3d XBlock is a XBlock where students can see and interact with 3d models"""

import pkg_resources
import os
import httplib2

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from django.template import Context,Template,RequestContext
from django.http import HttpResponse
from webob.response import Response


class ModelViewer(XBlock):

    display_name = String(display_name="Display name", default="mt3d", scope=Scope.settings , help="Name of component in edxplatform")
    title = String(default="Title", scope=Scope.content, help="Enter Title")
    model3d =  String(default="http://edxstatic.extensionengine.com/slider/3d/buckyball/BuckyBall_molecular_structure.obj", scope=Scope.content, help="Enter a adress of model")
    background1 = String(default="#ffffff", scope=Scope.content, help="Enter a first half of background")
    background2 = String(default="#383840", scope=Scope.content, help="Enter a second half of background")
    pict_name = String(default="",scope=Scope.content, help="Enter image name")
    height = Integer(default=400 ,scope=Scope.content, help="Height of model viewer")
    width  = Integer(default=750 ,scope=Scope.content, help="Width of model viewer")


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """
        The primary view of the ModelViewer, shown to students
        when viewing courses.
        """

        template_str = self.resource_string("static/html/mt3d.html")
        template = Template(template_str)
        html = template.render(Context({
            'lres':self.model3d,
            'lword':self.title,
            'bg1':self.background1,
            'bg2':self.background2,
            'height':self.height,
            'width':self.width
            }))

        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/mt3d.css"))
        frag.add_javascript(self.resource_string("static/js/src/mt3d.js"))
        frag.add_javascript(self.resource_string("static/js/lib/jsc3d.js"))
        frag.add_javascript(self.resource_string("static/js/lib/jsc3d.webgl.js"))
        frag.add_javascript(self.resource_string("static/js/lib/jsc3d.touch.js"))
        frag.add_javascript(self.resource_string("static/js/lib/jsc3d.console.js"))
        frag.initialize_js('ModelViewer')
        return frag

    problem_view = student_view
   # studio_view = student_view


    def studio_view(self,context):
        """
        View for creating display the edit view  in Studio
        """

        html_ed_str=self.resource_string("static/html/mt3d_edit.html")
        word = self.title or ''
        frag = Fragment(html_ed_str.format(ltitle=self.title,loc=self.model3d,bg1=self.background1,bg2=self.background2,width=self.width,height=self.height))
        frag.add_javascript(self.resource_string("static/js/src/mt3d_edit.js"))
        frag.initialize_js('ModelViewerEdit')
        return frag

    @XBlock.json_handler
    def studio_submit(self,data,suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.title = data.get('word')
        self.model3d =  data.get('location')
        self.background1 = data.get('backgnd')
        self.background2 = data .get('backgnd1')
        self.height = data.get('height')
        self.width = data.get('width')

        return {'result':'success'}

    @XBlock.handler
    def upload_objfile(self,request,suffix=''):
        """
        Called when opening obj file
        """
        conn = httplib2.Http()
        if request.method == "GET":
            url = request.params['url']
            resp,content = conn.request(url,request.method)
            return Response(app_iter=content,content_type="text/plain")



    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ModelViewer",
             """<vertical_demo>
                <mt3d/>
                <mt3d/>
                </vertical_demo>
             """),
        ]





