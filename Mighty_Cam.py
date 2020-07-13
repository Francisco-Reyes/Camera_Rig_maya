## script para creacion una camara de 8 controles 4 libres y 4 dedicados###
import maya.cmds as cmds 

def hideAttributes(list_of_nodes,list_of_attributes):
    for node in list_of_nodes:
        for attribute in list_of_attributes:
            cmds.setAttr("{}.{}".format(node,attribute),lock=True,keyable=False,channelBox=False)
          

cmds.camera(name="riggedCam")
cmds.setAttr("riggedCamShape2.template", 1)
cmds.camera(name="freeCam")
cmds.setAttr("freeCam1.visibility", 0)
cmds.circle(name="cameraAim_CTR",radius=.3,normal=(0,0,0))
cmds.setAttr("cameraAim_CTRShape.overrideEnabled",1)
cmds.setAttr("cameraAim_CTRShape.overrideColor",17)
cmds.addAttr(longName="Follow",keyable=True,attributeType="enum",enumName="cam_CTR:world:")
cmds.circle(name="offsetAim_CTR",radius=.4,normal=(0,0,0))
cmds.setAttr("offsetAim_CTR.overrideEnabled",1)
cmds.setAttr("offsetAim_CTR.overrideColor",13)
cmds.select("cameraAim_CTR","offsetAim_CTR")
cmds.group(name="offsetAim_AUX")
cmds.group(name="offsetAim_OFF")
cmds.setAttr("offsetAim_OFF.translateZ", -5)
cmds.parent("cameraAim_CTR","offsetAim_CTR")
cmds.spaceLocator(name="camUpvec_LOC")
cmds.group(name="camUpvec_AUX")
cmds.group(name="camUpvec_OFF")
cmds.setAttr("camUpvec_OFF.translateY", 2)
cmds.setAttr("camUpvec_OFF.visibility", 0)
cmds.select("cameraAim_CTR","riggedCam1")
cmds.aimConstraint(maintainOffset=True,weight=1,aimVector=(1,0,0),upVector=(0,1,0),worldUpType="object",worldUpObject="camUpvec_LOC")
cmds.spaceLocator(name="worldAim_LOC")
cmds.group(name="worldAim_OFF")
cmds.setAttr("worldAim_OFF.translateZ", -5)
cmds.setAttr("worldAim_OFF.visibility", 0)
cmds.select("riggedCam1","camUpvec_OFF")
cmds.group(name="cameraGRP_AUX")
cmds.group(name="cameraGRP_OFF")

cmds.circle(name="Offset_CTR",normal=(0,1,0),radius=3.7)
cmds.setAttr("Offset_CTRShape.overrideEnabled",1)
cmds.setAttr("Offset_CTRShape.overrideColor", 20)
cmds.circle(name="Root_CTR",normal=(0,1,0),radius=3)
cmds.setAttr("Root_CTRShape.overrideEnabled",1)
cmds.setAttr("Root_CTRShape.overrideColor", 17)
cmds.curve(name="Dolly_CTR",bezier=True,degree=1,
point=[(-2.916862784320439, 0.0, -2.119246929e-16),
 (-1.9055496356322363, 0.0, 0.4666072733),
 (-1.9055496356322363, 0.0, 0.2333036366),
 (1.9055496356322363, 0.0, 0.2333036366),
 (1.9055496356322363, 0.0, 0.4666072733),
 (2.916862784320439, 0.0, 2.119246929e-16),
 (1.9055496356322363, 0.0, -0.4666072733),
 (1.9055496356322363, 0.0, -0.2333036366),
 (-1.9055496356322363, 0.0, -0.2333036366),
 (-1.9055496356322363, 0.0, -0.4666072733),
 (-2.916862784320439, 0.0, -2.119246929e-16)])
cmds.setAttr("bezierShape1.overrideEnabled",1)
cmds.setAttr("bezierShape1.overrideColor", 13)
cmds.curve(name="Travel_CTR",bezier=True,degree=1,
point=[(-4.238493858277452e-16, 0.0, 3.1397607292298555),
 (0.46660727329999996, 0.0, 2.291563015991779),
 (0.23330363659999995, 0.0, 2.2915630159917786),
 (0.23330363660000006, 0.0, -2.2915630159917777),
 (0.46660727330000007, 0.0, -2.2915630159917777),
 (4.238493858277452e-16, 0.0, -3.1397607292298555),
 (-0.46660727329999996, 0.0, -2.291563015991779),
 (-0.23330363659999995, 0.0, -2.2915630159917786),
 (-0.23330363660000006, 0.0, 2.2915630159917777),
 (-0.46660727330000007, 0.0, 2.2915630159917777),
 (-4.238493858277452e-16, 0.0, 3.1397607292298555)])
cmds.setAttr("bezierShape2.overrideEnabled",1)
cmds.setAttr("bezierShape2.overrideColor",6)
cmds.curve(name="Pedestal_CTR",bezier=True,degree=1,
point=[(-2.1192469290000005e-16, -0.9544239681, 2.1192469292774513e-16),
 (0.4666072733, -0.2545130582, 1.601208791113251e-16),
 (0.2333036366, -0.2545130582, 1.0831706527270058e-16),
 (0.2333036366, 0.2545130582, -4.709437639860419e-18),
 (0.4666072733, 0.2545130582, 4.709437619876412e-17),
 (2.1192469290000005e-16, 0.9544239681, -2.1192469292774513e-16),
 (-0.4666072733, 0.2545130582, -1.601208791113251e-16),
 (-0.2333036366, 0.2545130582, -1.0831706527270058e-16),
 (-0.2333036366, -0.2545130582, 4.709437639860419e-18),
 (-0.4666072733, -0.2545130582, -4.709437619876412e-17),
 (-2.1192469290000005e-16, -0.9544239681, 2.1192469292774513e-16)
])
cmds.setAttr("bezierShape3.overrideEnabled",1)
cmds.setAttr("bezierShape3.overrideColor",9)
cmds.curve(name="Rotate_CTR",bezier=True,degree=1,
point=[(0.6388137899999999, 0.0, 1.7401155277826854),
 (0.6388137899999999, 0.0, 1.7401155277826854),
 (0.6388137899999999, 0.0, 1.7401155277826854),
 (0.2832699599999999, 0.0, 1.8186344977826856),
 (0.2832699599999999, 0.0, 1.8186344977826856),
 (0.2832699599999999, 0.0, 1.8186344977826856),
 (0.2832699599999999, 0.0, 1.8186344977826856),
 (0.88816986, 0.0, 1.4840105377826855),
 (0.88816986, 0.0, 1.4840105377826855),
 (0.88816986, 0.0, 1.4840105377826855),
 (0.88816986, 0.0, 1.4840105377826855),
 (0.8394183899999997, 0.0, 2.1735756877826855),
 (0.8394183899999997, 0.0, 2.1735756877826855),
 (0.8394183899999997, 0.0, 2.1735756877826855),
 (0.8394183899999997, 0.0, 2.1735756877826855),
 (0.7664511599999999, 0.0, 1.8374167777826855),
 (0.7664511599999999, 0.0, 1.8374167777826855),
 (0.7664511599999999, 0.0, 1.8374167777826855),
 (0.7664511599999999, 0.0, 1.8374167777826855),
 (0.6464067299999999, 0.0, 2.0295026077826854),
 (0.34986653999999984, 0.0, 2.2276715377826855),
 (-2.029985779472554e-16, 0.0, 2.2973072377826855),
 (-0.34986654000000017, 0.0, 2.2276715377826855),
 (-0.6464067300000002, 0.0, 2.0295026077826854),
 (-0.7648497900000001, 0.0, 1.8359207077826851),
 (-0.7648497900000001, 0.0, 1.8359207077826851),
 (-0.7648497900000001, 0.0, 1.8359207077826851),
 (-0.7648497900000001, 0.0, 1.8359207077826851),
 (-0.8394183900000002, 0.0, 2.173575687782685),
 (-0.8394183900000002, 0.0, 2.173575687782685),
 (-0.8394183900000002, 0.0, 2.173575687782685),
 (-0.8394183900000002, 0.0, 2.173575687782685),
 (-0.88816986, 0.0, 1.484010537782685),
 (-0.88816986, 0.0, 1.484010537782685),
 (-0.88816986, 0.0, 1.484010537782685),
 (-0.88816986, 0.0, 1.484010537782685),
 (-0.2832699600000001, 0.0, 1.8186344977826852),
 (-0.2832699600000001, 0.0, 1.8186344977826852),
 (-0.2832699600000001, 0.0, 1.8186344977826852),
 (-0.2832699600000001, 0.0, 1.8186344977826852),
 (-0.6363206100000001, 0.0, 1.7388341077826852),
 (-0.6363206100000001, 0.0, 1.7388341077826852),
 (-0.6363206100000001, 0.0, 1.7388341077826852),
 (-0.6363206100000001, 0.0, 1.7388341077826852),
 (-0.5289283800000001, 0.0, 1.9118314777826853),
 (-0.28621998000000015, 0.0, 2.0741919277826852),
 (-1.6607303532367722e-16, 0.0, 2.1310093777826853),
 (0.2862199799999998, 0.0, 2.0741919277826857),
 (0.5289283799999999, 0.0, 1.9118314777826857),
 (0.6388137899999999, 0.0, 1.7401155277826854),
 (6.256799078840915e-17, -0.63881379, 1.7401155277826854),
 (6.256799078840915e-17, -0.63881379, 1.7401155277826854),
 (6.256799078840915e-17, -0.63881379, 1.7401155277826854),
 (-3.381331215024375e-17, -0.28326996, 1.8186344977826856),
 (-3.381331215024375e-17, -0.28326996, 1.8186344977826856),
 (-3.381331215024375e-17, -0.28326996, 1.8186344977826856),
 (-3.381331215024375e-17, -0.28326996, 1.8186344977826856),
 (1.7480289216109668e-16, -0.88816986, 1.4840105377826855),
 (1.7480289216109668e-16, -0.88816986, 1.4840105377826855),
 (1.7480289216109668e-16, -0.88816986, 1.4840105377826855),
 (1.7480289216109668e-16, -0.88816986, 1.4840105377826855),
 (1.0863669963612211e-17, -0.83941839, 2.1735756877826855),
 (1.0863669963612211e-17, -0.83941839, 2.1735756877826855),
 (1.0863669963612211e-17, -0.83941839, 2.1735756877826855),
 (1.0863669963612211e-17, -0.83941839, 2.1735756877826855),
 (6.930396256876748e-17, -0.76645116, 1.8374167777826855),
 (6.930396256876748e-17, -0.76645116, 1.8374167777826855),
 (6.930396256876748e-17, -0.76645116, 1.8374167777826855),
 (6.930396256876748e-17, -0.76645116, 1.8374167777826855),
 (-2.8776980798174786e-21, -0.64640673, 2.0295026077826854),
 (-1.0985036880128973e-16, -0.34986654, 2.2276715377826855),
 (-2.029985779472554e-16, 0.0, 2.2973072377826855),
 (-2.6522232410286505e-16, 0.34986654, 2.2276715377826855),
 (-2.870651316655426e-16, 0.64640673, 2.0295026077826854),
 (-2.7038095762321745e-16, 0.76484979, 1.8359207077826856),
 (-2.7038095762321745e-16, 0.76484979, 1.8359207077826856),
 (-2.7038095762321745e-16, 0.76484979, 1.8359207077826856),
 (-2.7038095762321745e-16, 0.76484979, 1.8359207077826856),
 (-3.6191297958509945e-16, 0.83941839, 2.1735756877826855),
 (-3.6191297958509945e-16, 0.83941839, 2.1735756877826855),
 (-3.6191297958509945e-16, 0.83941839, 2.1735756877826855),
 (-3.6191297958509945e-16, 0.83941839, 2.1735756877826855),
 (-2.1962375917894405e-16, 0.88816986, 1.4840105377826855),
 (-2.1962375917894405e-16, 0.88816986, 1.4840105377826855),
 (-2.1962375917894405e-16, 0.88816986, 1.4840105377826855),
 (-2.1962375917894405e-16, 0.88816986, 1.4840105377826855),
 (-1.5961044486090259e-16, 0.28326996, 1.8186344977826856),
 (-1.5961044486090259e-16, 0.28326996, 1.8186344977826856),
 (-1.5961044486090259e-16, 0.28326996, 1.8186344977826856),
 (-1.5961044486090259e-16, 0.28326996, 1.8186344977826856),
 (-2.2028419088826466e-16, 0.63632061, 1.7388341077826852),
 (-2.2028419088826466e-16, 0.63632061, 1.7388341077826852),
 (-2.2028419088826466e-16, 0.63632061, 1.7388341077826852),
 (-2.2028419088826466e-16, 0.63632061, 1.7388341077826852),
 (-2.34851458280616e-16, 0.52892838, 1.9118314777826853),
 (-2.1701062946632986e-16, 0.28621998, 2.0741919277826852),
 (-1.6607303532367722e-16, 0.0, 2.1310093777826853),
 (-8.990342470482916e-17, -0.28621998, 2.0741919277826852),
 (3.9928060857606183e-20, -0.52892838, 1.9118314777826853),
 (6.256799078840915e-17, -0.63881379, 1.7401155277826854)])
cmds.setAttr("bezierShape4.overrideEnabled",1)
cmds.setAttr("bezierShape4.overrideColor",18)
cmds.circle(name="Cam_CTR",normal=(0,0,1),radius=1)
cmds.setAttr("Cam_CTRShape.overrideEnabled",1)
cmds.setAttr("Cam_CTRShape.overrideColor",20)
cmds.curve(name="CP_CTR",bezier=True,degree=1,
point=[(-0.5127616300904922, 0.0, -1.138559535741584e-16),
 (-0.2825421227188484, 0.0, 0.15347967159843545),
 (-0.2825421227188484, 0.0, 0.0767398357732088),
 (-0.07673983577320885, 0.0, 0.07673983577320885),
 (-0.07673983577320885, 0.0, 0.2825421227188484),
 (-0.1534796715984356, 0.0, 0.2825421227188483),
 (-1.138559535741584e-16, 0.0, 0.5127616300904922),
 (0.15347967159843545, 0.0, 0.2825421227188484),
 (0.0767398357732088, 0.0, 0.2825421227188484),
 (0.07673983577320885, 0.0, 0.07673983577320885),
 (0.2825421227188484, 0.0, 0.07673983577320885),
 (0.2825421227188483, 0.0, 0.1534796715984356),
 (0.5127616300904922, 0.0, 1.138559535741584e-16),
 (0.2825421227188484, 0.0, -0.15347967159843545),
 (0.2825421227188484, 0.0, -0.0767398357732088),
 (0.07673983577320885, 0.0, -0.07673983577320885),
 (0.07673983577320885, 0.0, -0.2825421227188484),
 (0.1534796715984356, 0.0, -0.2825421227188483),
 (1.138559535741584e-16, 0.0, -0.5127616300904922),
 (-0.15347967159843545, 0.0, -0.2825421227188484),
 (-0.0767398357732088, 0.0, -0.2825421227188484),
 (-0.07673983577320885, 0.0, -0.07673983577320885),
 (-0.2825421227188484, 0.0, -0.07673983577320885),
 (-0.2825421227188483, 0.0, -0.1534796715984356),
 (-0.5127616300904922, 0.0, -1.138559535741584e-16)])
cmds.setAttr("bezierShape5.overrideEnabled",1)
cmds.setAttr("bezierShape5.overrideColor",28)
 
cmds.curve(name="HUD_CTR",bezier=True,degree=1,
point=[(0.27845484408537857, 0.15530758122284458, -0.692456556519762),
 (0.27845484408537857, 0.17477602399160894, -0.692456556519762),
 (0.2745611555316257, 0.17477602399160894, -0.692456556519762),
 (0.2745611555316257, 0.1669886468841032, -0.692456556519762),
 (0.27066746697787286, 0.1669886468841032, -0.692456556519762),
 (0.27066746697787286, 0.17477602399160894, -0.692456556519762),
 (0.26677377842412, 0.17477602399160894, -0.692456556519762),
 (0.26677377842412, 0.15530758122284458, -0.692456556519762),
 (0.27066746697787286, 0.15530758122284458, -0.692456556519762),
 (0.27066746697787286, 0.16309495833035031, -0.692456556519762),
 (0.2745611555316257, 0.16309495833035031, -0.692456556519762),
 (0.2745611555316257, 0.15530758122284458, -0.692456556519762),
 (0.28234853263913146, 0.15530758122284458, -0.692456556519762),
 (0.28234853263913146, 0.17477602399160894, -0.692456556519762),
 (0.28624222119288434, 0.17477602399160894, -0.692456556519762),
 (0.28624222119288434, 0.15920126977659746, -0.692456556519762),
 (0.2901359097466372, 0.15920126977659746, -0.692456556519762),
 (0.2901359097466372, 0.17477602399160894, -0.692456556519762),
 (0.29402959830039005, 0.17477602399160894, -0.692456556519762),
 (0.29402959830039005, 0.15530758122284458, -0.692456556519762),
 (0.28234853263913146, 0.15530758122284458, -0.692456556519762),
 (0.29792328685414293, 0.15530758122284458, -0.692456556519762),
 (0.29792328685414293, 0.17477602399160894, -0.692456556519762),
 (0.3057106639616487, 0.17477602399160894, -0.692456556519762),
 (0.3096043525154015, 0.17088233543785608, -0.692456556519762),
 (0.3096043525154015, 0.15920126977659746, -0.692456556519762),
 (0.3057106639616487, 0.15530758122284458, -0.692456556519762),
 (0.29792328685414293, 0.15530758122284458, -0.692456556519762),
 (0.29792328685414293, 0.17088233543785608, -0.692456556519762),
 (0.3018169754078958, 0.17088233543785608, -0.692456556519762),
 (0.3057106639616487, 0.1669886468841032, -0.692456556519762),
 (0.3057106639616487, 0.16309495833035031, -0.692456556519762),
 (0.3018169754078958, 0.15920126977659746, -0.692456556519762),
 (0.3018169754078958, 0.17088233543785608, -0.692456556519762)])
cmds.setAttr("bezierShape6.overrideEnabled",1)
cmds.setAttr("bezierShape6.overrideColor",17)

cmds.curve(name="Shake_CTR",bezier=True,degree=1,
point=[(-0.5102108146460248, 0.5652693534737985, 3.323285603015268),
 (-0.7653162219690373, 0.5652693534737985, 3.323285603015268),
 (-0.7653162219690373, 0.650304489248136, 3.323285603015268),
 (-0.5952459504203622, 0.650304489248136, 3.323285603015268),
 (-0.5952459504203622, 0.7353396250224735, 3.323285603015268),
 (-0.7653162219690373, 0.7353396250224735, 3.323285603015268),
 (-0.7653162219690373, 0.9904450323454859, 3.323285603015268),
 (-0.5102108146460248, 0.9904450323454859, 3.323285603015268),
 (-0.5102108146460248, 0.9054098965711483, 3.323285603015268),
 (-0.6802810861946997, 0.9054098965711483, 3.323285603015268),
 (-0.6802810861946997, 0.8203747607968109, 3.323285603015268),
 (-0.5102108146460248, 0.8203747607968109, 3.323285603015268),
 (-0.5102108146460248, 0.5652693534737985, 3.323285603015268),
 (-0.42517567887168733, 0.5652693534737985, 3.323285603015268),
 (-0.42517567887168733, 0.9904450323454859, 3.323285603015268),
 (-0.34014054309734987, 0.9904450323454859, 3.323285603015268),
 (-0.34014054309734987, 0.8203747607968109, 3.323285603015268),
 (-0.2551054073230124, 0.8203747607968109, 3.323285603015268),
 (-0.2551054073230124, 0.9904450323454859, 3.323285603015268),
 (-0.17007027154867493, 0.9904450323454859, 3.323285603015268),
 (-0.17007027154867493, 0.5652693534737985, 3.323285603015268),
 (-0.2551054073230124, 0.5652693534737985, 3.323285603015268),
 (-0.2551054073230124, 0.7353396250224735, 3.323285603015268),
 (-0.34014054309734987, 0.7353396250224735, 3.323285603015268),
 (-0.34014054309734987, 0.5652693534737985, 3.323285603015268),
 (-0.42517567887168733, 0.5652693534737985, 3.323285603015268),
 (-0.08503513577433747, 0.5652693534737985, 3.323285603015268),
 (-0.08503513577433747, 0.9904450323454859, 3.323285603015268),
 (0.17007027154867493, 0.9904450323454859, 3.323285603015268),
 (0.17007027154867493, 0.5652693534737985, 3.323285603015268),
 (0.08503513577433747, 0.5652693534737985, 3.323285603015268),
 (0.08503513577433747, 0.9054098965711483, 3.323285603015268),
 (0.0, 0.9054098965711483, 3.323285603015268),
 (0.0, 0.8203747607968109, 3.323285603015268),
 (0.08503513577433747, 0.8203747607968109, 3.323285603015268),
 (0.08503513577433747, 0.7353396250224735, 3.323285603015268),
 (0.0, 0.7353396250224735, 3.323285603015268),
 (0.0, 0.5652693534737985, 3.323285603015268),
 (-0.08503513577433747, 0.5652693534737985, 3.323285603015268),
 (0.2551054073230124, 0.5652693534737985, 3.323285603015268),
 (0.2551054073230124, 0.9904450323454859, 3.323285603015268),
 (0.34014054309734987, 0.9904450323454859, 3.323285603015268),
 (0.34014054309734987, 0.8203747607968109, 3.323285603015268),
 (0.42517567887168733, 0.9904450323454859, 3.323285603015268),
 (0.5102108146460248, 0.9904450323454859, 3.323285603015268),
 (0.39353469811844544, 0.7650030444786565, 3.323285603015268),
 (0.5102108146460248, 0.5652693534737985, 3.323285603015268),
 (0.42517567887168733, 0.5652693534737985, 3.323285603015268),
 (0.34014054309734987, 0.7353396250224735, 3.323285603015268),
 (0.34014054309734987, 0.5652693534737985, 3.323285603015268),
 (0.2551054073230124, 0.5652693534737985, 3.323285603015268),
 (0.5952459504203622, 0.5652693534737985, 3.323285603015268),
 (0.5952459504203622, 0.9904450323454859, 3.323285603015268),
 (0.8503513577433747, 0.9904450323454859, 3.323285603015268),
 (0.8503513577433747, 0.9054098965711483, 3.323285603015268),
 (0.6802810861946997, 0.9054098965711483, 3.323285603015268),
 (0.6802810861946997, 0.8203747607968109, 3.323285603015268),
 (0.7653162219690373, 0.8203747607968109, 3.323285603015268),
 (0.7653162219690373, 0.7353396250224735, 3.323285603015268),
 (0.6802810861946997, 0.7353396250224735, 3.323285603015268),
 (0.6802810861946997, 0.650304489248136, 3.323285603015268),
 (0.8503513577433747, 0.650304489248136, 3.323285603015268),
 (0.8503513577433747, 0.5652693534737985, 3.323285603015268),
 (-0.9353864935177121, 0.5652693534737985, 3.323285603015268),
 (-0.9353864935177121, 1.1605153038941607, 3.323285603015268),
 (1.0204216292920496, 1.1605153038941607, 3.323285603015268),
 (1.0204216292920496, 0.3951990819251236, 3.323285603015268),
 (-0.9353864935177121, 0.3951990819251236, 3.323285603015268),
 (-0.9353864935177121, 0.5652693534737985, 3.323285603015268)])
cmds.setAttr("bezierShape7.overrideEnabled",1)
cmds.setAttr("bezierShape7.overrideColor",13)
cmds.group(name="Shake_AUX")
 
items = cmds.ls("Offset_CTR","Root_CTR","Dolly_CTR","Travel_CTR","Pedestal_CTR","Rotate_CTR","Cam_CTR","CP_CTR")

for item in items:
 	auxGRP=cmds.group(empty=True)
 	cmds.parent(item,auxGRP)
 	auxName = item.replace("CTR","AUX")
 	cmds.rename(auxGRP,auxName)
 	offGRP=cmds.group(empty=True)
 	cmds.parent(auxName,offGRP)
 	cmds.rename(auxGRP,auxName.replace("AUX","OFF"))

cmds.polyPlane(name="cinema3rds",subdivisionsX=3,subdivisionsY=3,axis=(0,0,1))
cmds.setAttr("cinema3rds.translateZ", -1.991)
cmds.setAttr("cinema3rds.translateY", .001)
cmds.setAttr("cinema3rds.scaleX", 2.05)
cmds.setAttr("cinema3rds.scaleY", 1.16)
cmds.setAttr("cinema3rdsShape.template", 1)

cmds.polyPlane(name="golden3rds",subdivisionsX=3,subdivisionsY=3,axis=(0,0,1))
cmds.setAttr("golden3rds.translateZ", -1.991)
cmds.setAttr("golden3rds.scaleX", 2.07)
cmds.setAttr("golden3rds.scaleY", 1.161)
cmds.select("golden3rds.vtx[2]","golden3rds.vtx[6]","golden3rds.vtx[10]","golden3rds.vtx[14]")
cmds.move(-0.109545,0,0, relative=True,objectSpace=True,worldSpaceDistance=True) 
cmds.select("golden3rds.vtx[1]","golden3rds.vtx[5]","golden3rds.vtx[9]","golden3rds.vtx[13]")
cmds.move(0.104225,0,0, relative=True,objectSpace=True,worldSpaceDistance=True)
cmds.select("golden3rds.vtx[8:11]")
cmds.move(0,-.0739309,0, relative=True,objectSpace=True,worldSpaceDistance=True)
cmds.select("golden3rds.vtx[4:7]")
cmds.move(0,.0270455,0, relative=True,objectSpace=True,worldSpaceDistance=True)
cmds.setAttr("golden3rdsShape.template", 1)

cmds.polyPlane(name="goldenTriangle",subdivisionsX=3,subdivisionsY=2,axis=(0,0,1))
cmds.setAttr("goldenTriangle.translateZ",-1.991)
cmds.setAttr("goldenTriangle.scaleX", 2.401)
cmds.setAttr("goldenTriangle.scaleY", 2.1)
cmds.setAttr("goldenTriangle.rotateZ", 29.28)
cmds.select("goldenTriangle.vtx[2]","goldenTriangle.vtx[6]","goldenTriangle.vtx[10]")
cmds.move(0.212443,.006697407,0,relative=True,objectSpace=True,worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[1]","goldenTriangle.vtx[5]",
"goldenTriangle.vtx[9]")
cmds.move(-0.2130638,-0.007333978,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[1]")
cmds.move(.0029139,.700500909,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[0]")
cmds.move(.0466315,.987488,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[11]")
cmds.move(-.0464467,-.983576,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[10]")
cmds.move(-.01414795,-.665673707,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[8]")
cmds.move(.2094896,-.4830333,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.select("goldenTriangle.vtx[3]")
cmds.move(-.327251,.413532,0,relative=True,objectSpace=True,
worldSpaceDistance=True)
cmds.setAttr("goldenTriangle.template", 1)
cmds.select("goldenTriangle")
cmds.duplicate()
cmds.select("goldenTriangle1")
cmds.group(name="harmoniousTriangle")
cmds.setAttr("harmoniousTriangle.rotateY", 180)

cmds.polyPlane(name="cu1",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu1.translateZ", -1.991)
cmds.setAttr("cu1.translateX", -0.401)
cmds.setAttr("cu1.scaleX", 1.267)
cmds.setAttr("cu1.scaleY", 1.157)
cmds.setAttr("cu1.template", 1)
cmds.polyPlane(name="cu2",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu2.translateZ", -1.991)
cmds.setAttr("cu2.translateY", -0.25)
cmds.setAttr("cu2.translateX", 0.636)
cmds.setAttr("cu2.scaleX", .795)
cmds.setAttr("cu2.scaleY", .707)
cmds.setAttr("cu2.template", 1)
cmds.polyPlane(name="cu3",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu3.translateZ", -1.991)
cmds.setAttr("cu3.translateY", 0.346)
cmds.setAttr("cu3.translateX", 0.636)
cmds.setAttr("cu3.scaleX", .795)
cmds.setAttr("cu3.scaleY", .484)
cmds.setAttr("cu3.template", 1)
cmds.polyPlane(name="cu4",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu4.translateZ", -1.991)
cmds.setAttr("cu4.translateY", 0.346)
cmds.setAttr("cu4.translateX", 0.388)
cmds.setAttr("cu4.scaleX", .3)
cmds.setAttr("cu4.scaleY", .484)
cmds.setAttr("cu4.template", 1)
cmds.polyPlane(name="cu5",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu5.translateZ", -1.991)
cmds.setAttr("cu5.translateY", .196)
cmds.setAttr("cu5.translateX", .388)
cmds.setAttr("cu5.scaleY", .182)
cmds.setAttr("cu5.scaleX", .3)
cmds.setAttr("cu5.template", 1)
cmds.polyPlane(name="cu6",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu6.translateZ", -1.991)
cmds.setAttr("cu6.translateY", 0.197)
cmds.setAttr("cu6.translateX", 0.493)
cmds.setAttr("cu6.scaleX", .09)
cmds.setAttr("cu6.scaleY", .18)
cmds.setAttr("cu6.template", 1)
cmds.polyPlane(name="cu7",subdivisionsX=1,subdivisionsY=1,
axis=(0,0,1))
cmds.setAttr("cu7.translateZ", -1.991)
cmds.setAttr("cu7.translateY", 0.253)
cmds.setAttr("cu7.translateX", 0.493)
cmds.setAttr("cu7.scaleX", .09)
cmds.setAttr("cu7.scaleY", .069)
cmds.setAttr("cu7.template", 1)
cmds.select("cu1","cu2","cu3","cu4","cu5","cu6","cu7")
cmds.group(name="goldenSpiralSections")

cmds.select("cinema3rds","golden3rds","goldenTriangle","harmoniousTriangle",
"goldenSpiralSections","HUD_CTR")

cmds.group(name="Cam_Grids")
cmds.select("riggedCam1","Cam_Grids")
cmds.parentConstraint(maintainOffset=True,name="gridsFollow")
	
cmds.parent("cameraGRP_OFF","CP_CTR")
cmds.parent("CP_OFF","Cam_CTR")
cmds.parent("Cam_OFF","Rotate_CTR")
cmds.parent("Rotate_OFF","Pedestal_CTR")
cmds.parent("Pedestal_OFF","Travel_CTR")
cmds.parent("Travel_OFF","Dolly_CTR")
cmds.parent("Dolly_OFF","Root_CTR")
cmds.parent("Root_OFF","Offset_CTR")
cmds.parent("Shake_AUX","CP_CTR")
cmds.parent("Cam_Grids","Offset_AUX")
cmds.parent("offsetAim_OFF","Offset_AUX")
cmds.parent("worldAim_OFF","Offset_AUX")


list_of_nodes=["Offset_CTR","Root_CTR","Dolly_CTR","Travel_CTR","Pedestal_CTR","Rotate_CTR","Cam_CTR","CP_CTR","offsetAim_CTR","cameraAim_CTR","Shake_CTR","HUD_CTR"]
list_of_attributes=['visibility','scaleX','scaleY','scaleZ'] 
hideAttributes(list_of_nodes,list_of_attributes)

new_nodes=["cameraAim_CTR","offsetAim_CTR","Dolly_CTR","Travel_CTR","Pedestal_CTR","Shake_CTR","HUD_CTR"]
new_attributes=["rotateX","rotateY","rotateZ"]
hideAttributes(new_nodes,new_attributes)

trans_nodes=["Rotate_CTR","Shake_CTR","HUD_CTR"]
trans_attributes=["translateX","translateY","translateZ"]
hideAttributes(trans_nodes,trans_attributes)

cmds.setAttr("Dolly_CTR.translateY",lock=True,keyable=False,channelBox=False)
cmds.setAttr("Dolly_CTR.translateZ",lock=True,keyable=False,channelBox=False)
cmds.setAttr("Travel_CTR.translateX",lock=True,keyable=False,channelBox=False)
cmds.setAttr("Travel_CTR.translateY",lock=True,keyable=False,channelBox=False)
cmds.setAttr("Pedestal_CTR.translateX",lock=True,keyable=False,channelBox=False)
cmds.setAttr("Pedestal_CTR.translateZ",lock=True,keyable=False,channelBox=False)
cmds.select("Offset_CTR")
cmds.addAttr(longName="follow",attributeType="bool",keyable=True)
cmds.select("HUD_CTR")
cmds.addAttr(longName="Lens",keyable=True,defaultValue=35)
cmds.addAttr(longName="Near_Clip",keyable=True,defaultValue=.01)
cmds.addAttr(longName="Far_Clip",keyable=True,defaultValue=100000000)
cmds.addAttr(longName="Displayables",keyable=False,attributeType="enum",enumName="____:")
cmds.setAttr("HUD_CTR.Displayables",edit=True,channelBox=True)
cmds.addAttr(longName="Aim_Vis",keyable=False,attributeType="bool")
cmds.setAttr("HUD_CTR.Aim_Vis",edit=True,channelBox=True)
cmds.addAttr(longName="Field_Chart",keyable=False,attributeType="bool")
cmds.setAttr("HUD_CTR.Field_Chart",edit=True,channelBox=True)
cmds.addAttr(longName="Safe_Action",keyable=False,attributeType="bool")
cmds.setAttr("HUD_CTR.Safe_Action",edit=True,channelBox=True)
cmds.addAttr(longName="Safe_Title",keyable=False,attributeType="bool")
cmds.setAttr("HUD_CTR.Safe_Title",edit=True,channelBox=True)
cmds.addAttr(longName="Shake",keyable=False,attributeType="bool")
cmds.setAttr("HUD_CTR.Shake",edit=True,channelBox=True)
cmds.addAttr(longName="Composition",keyable=False,attributeType="enum",enumName="OFF:GoldenSection:GoldenSpiralSection:GoldenTriangle:HarmoniousTriangle:RuleOfThirds")
cmds.setAttr("HUD_CTR.Composition",edit=True,channelBox=True)
cmds.select("Shake_CTR")
cmds.addAttr(longName="Shake",keyable=True,attributeType="bool")
cmds.addAttr(longName="Hrzt_Amplitud",keyable=True)
cmds.addAttr(longName="Hrzt_Frequency",keyable=True)
cmds.addAttr(longName="Vert_Amplitud",keyable=True)
cmds.addAttr(longName="Vert_Frequency",keyable=True)


cmds.connectAttr("HUD_CTR.Aim_Vis","offsetAim_AUX.visibility")
cmds.connectAttr("HUD_CTR.Shake","Shake_AUX.visibility")
cmds.connectAttr("HUD_CTR.Field_Chart","riggedCamShape2.displayFieldChart")
cmds.connectAttr("HUD_CTR.Safe_Action","riggedCamShape2.displaySafeAction")
cmds.connectAttr("HUD_CTR.Safe_Title","riggedCamShape2.displaySafeTitle")
cmds.connectAttr("HUD_CTR.Lens","riggedCamShape2.focalLength")
cmds.connectAttr("HUD_CTR.Near_Clip","riggedCamShape2.nearClipPlane")
cmds.connectAttr("HUD_CTR.Far_Clip","riggedCamShape2.farClipPlane")
cmds.shadingNode("condition", asUtility=True,name="gtconnect")
cmds.setAttr("gtconnect.secondTerm", 3)
cmds.setAttr("gtconnect.colorIfFalseR", 0)
cmds.setAttr("gtconnect.colorIfTrueR", 1)
cmds.shadingNode("condition", asUtility=True,name="htconnect")
cmds.setAttr("htconnect.secondTerm", 4)
cmds.setAttr("htconnect.colorIfFalseR", 0)
cmds.setAttr("htconnect.colorIfTrueR", 1)
cmds.shadingNode("condition", asUtility=True,name="gssconnect")
cmds.setAttr("gssconnect.secondTerm", 2)
cmds.setAttr("gssconnect.colorIfFalseR", 0)
cmds.setAttr("gssconnect.colorIfTrueR", 1)
cmds.shadingNode("condition", asUtility=True,name="g3connect")
cmds.setAttr("g3connect.secondTerm", 1)
cmds.setAttr("g3connect.colorIfFalseR", 0)
cmds.setAttr("g3connect.colorIfTrueR", 1)
cmds.shadingNode("condition", asUtility=True,name="c3connect")
cmds.setAttr("c3connect.secondTerm", 5)
cmds.setAttr("c3connect.colorIfFalseR", 0)
cmds.setAttr("c3connect.colorIfTrueR", 1)
cmds.connectAttr("HUD_CTR.Composition","c3connect.firstTerm")	
cmds.connectAttr("HUD_CTR.Composition","g3connect.firstTerm")	
cmds.connectAttr("HUD_CTR.Composition","gssconnect.firstTerm")	
cmds.connectAttr("HUD_CTR.Composition","gtconnect.firstTerm")	
cmds.connectAttr("HUD_CTR.Composition","htconnect.firstTerm")
cmds.connectAttr("c3connect.outColor.outColorR","cinema3rds.visibility")	
cmds.connectAttr("g3connect.outColor.outColorR","golden3rds.visibility")	
cmds.connectAttr("gssconnect.outColor.outColorR","goldenSpiralSections.visibility")	
cmds.connectAttr("gtconnect.outColor.outColorR","goldenTriangle.visibility")	
cmds.connectAttr("htconnect.outColor.outColorR","harmoniousTriangle.visibility")	


cmds.shadingNode("multiplyDivide",asUtility=True,name="GridsDiv")
cmds.setAttr("GridsDiv.operation", 2)
cmds.setAttr("GridsDiv.input1.input1X", 35)
cmds.setAttr("GridsDiv.input1.input1Y", 35)
cmds.connectAttr("riggedCamShape2.focalLength","GridsDiv.input2.input2X")
cmds.connectAttr("riggedCamShape2.focalLength","GridsDiv.input2.input2Y")
cmds.connectAttr("GridsDiv.output.outputX","Cam_Grids.scaleX")
cmds.connectAttr("GridsDiv.output.outputY","Cam_Grids.scaleY")

cmds.select("CP_CTR","worldAim_LOC","offsetAim_AUX")
cmds.parentConstraint(maintainOffset=True,name="aimFollow_pc")
cmds.shadingNode("reverse",asUtility=True,name="AimReverse")
cmds.connectAttr("cameraAim_CTR.Follow","AimReverse.input.inputX")
cmds.connectAttr("cameraAim_CTR.Follow","aimFollow_pc.worldAim_LOCW1")
cmds.connectAttr("AimReverse.output.outputX","aimFollow_pc.CP_CTRW0")

cmds.shadingNode("multiplyDivide",asUtility=True,name="timeXfrq")
cmds.shadingNode("multiplyDivide",asUtility=True,name="frqXamp")
cmds.shadingNode("multiplyDivide",asUtility=True,name="ampXnoise")
cmds.connectAttr("time1.outTime","timeXfrq.input1.input1X")
cmds.connectAttr("time1.outTime","timeXfrq.input1.input1Y")
cmds.connectAttr("Shake_CTR.Hrzt_Frequency","timeXfrq.input2.input2X")
cmds.connectAttr("Shake_CTR.Vert_Frequency","timeXfrq.input2.input2Y")
cmds.connectAttr("timeXfrq.output.outputX","frqXamp.input1.input1X")
cmds.connectAttr("timeXfrq.output.outputY","frqXamp.input1.input1Y")
cmds.connectAttr("Shake_CTR.Hrzt_Amplitud","frqXamp.input2.input2X")
cmds.connectAttr("Shake_CTR.Vert_Amplitud","frqXamp.input2.input2Y")
cmds.connectAttr("frqXamp.output.outputX","ampXnoise.input1.input1X")
cmds.connectAttr("frqXamp.output.outputY","ampXnoise.input1.input1Y")
cmds.shadingNode("noise",asTexture=True,name="noiseShake")
cmds.connectAttr("time1.outTime","noiseShake.time")
cmds.connectAttr("noiseShake.outColor.outColorR","ampXnoise.input2.input2X")
cmds.connectAttr("noiseShake.outColor.outColorR","ampXnoise.input2.input2Y")
cmds.shadingNode("multiplyDivide", asUtility=True,name="limiter")
cmds.setAttr("limiter.operation",2)
cmds.setAttr("limiter.input2.input2X", 2000)
cmds.setAttr("limiter.input2.input2Y", 2000)
cmds.connectAttr("ampXnoise.output.outputX","limiter.input1.input1X")
cmds.connectAttr("ampXnoise.output.outputY","limiter.input1.input1Y")
cmds.shadingNode("multiplyDivide", asUtility=True,name="onOff")
cmds.connectAttr("limiter.output.outputX","onOff.input1.input1X")
cmds.connectAttr("limiter.output.outputY","onOff.input1.input1Y")
cmds.connectAttr("Shake_CTR.Shake","onOff.input2.input2X")
cmds.connectAttr("Shake_CTR.Shake","onOff.input2.input2Y")
cmds.connectAttr("onOff.output.outputX","cameraGRP_AUX.rotateX")
cmds.connectAttr("onOff.output.outputY","cameraGRP_AUX.rotateY")

cmds.select("freeCam1","Root_AUX")
cmds.parentConstraint(maintainOffset=True,name="rigFollow")
cmds.connectAttr("Offset_CTR.follow","rigFollow.freeCam1W0")

cmds.select("freeCam1","Offset_OFF")
cmds.group(name="CameraRig_GRP")


     







