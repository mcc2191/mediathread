<fsi_parameter>

  <licence domains="artstor.org">
    sOOmgEE9xa.9XOxXOgXrdJx.CE9aXTOXmr2COCdTXsmdXa2Xx2TgJEaE.Or.
    T9gga92JmssJCrsaJ.xrXXdrxa2JgCmrddO99gCEXsTmJrXsO2OdmJaX.s.g
    sOsXmm..2mTsdgr.OJOxm2.X9Jdr.Jd.OETXaXxJJrXX9aTTCxmEmmXTTsXd
    mXdOdJCEsgaa.EXd2dEsCC9OJOXTrs9daO.JrrCT9mTr2CxXarJs2d.9XxE9
    TEXTrx.ma99.rTTCg.9.mgJdCs2dsJsgmr.grgmOE9OO.dgCOdJm92m9OOdC
    Od2O2adEgJJmTXs9C.2TCE..OOOxraEOrsO2sXsTCa..msx.9XJ22m2JE29d
    CXxTTmEdEasTXTsxX2E9EJErmgdgrdXJXCmaC.2Jg2m..CxCEaxsCTXaTCaJ
    mss92Ox2g9JdrgXrTmxCOxXCXr2xJsJdrJ2TOExg9OmCXa
  </licence>

        <FPX>
<!--            <ServerType value="eRez" />
                <!-- Enter absolute path to imaging server -->
                <Base value="http://webcache.artstor.org/erez3/erez?src=" />
                <Base value="http://imgserver.artstor.net/" />
-->
                <ServerType value="TrueSpectra" />
                <Base value="http://192.168.11.247/" />
        </FPX>

        <PLUGINS>
                <PLUGIN src="resize" MinWidth="300" MinWidth="100" MaxWidth="5000" maxHeight="5000" EnlargeBy="1"/>
                <PLUGIN src="mousemodes" Menuoffset="10" Mode2="false" default="100" />         
                <PLUGIN src="zoommeter" SrcRelative="1"/>
                <plugin src="jsbridge" callback="true" ImageUrls="true" explore="true" >
                <allowdomains value="artstor.org,*,192.168.11.72:8080,webcache.artstor.org,viewer.artstor.org,192.168.11.228:7777,localhost:8080,viewer2.stage.artstor.org,viewer2.artstor.org" />
                <callback value="true" />
                </plugin>
<!--                <PLUGIN src="custombutton" MenuOffset="10" buttons="Btn1,Btn2,Btn3" Btn1.Url="javascript: void printImage('$$URLView$$')" Btn1.Tooltip="P
rint Current View" Btn1.LabelFrame="7" Btn2.Url="javascript:void saveImage('$$URLView$$');" Btn2.Tooltip="Save Current View" Btn2.LabelFrame="6" Btn3.Url="ja
vascript:void saveToImageGroup();" Btn3.Tooltip="Save to Image Group" Btn3.LabelFrame="8" /> --> 
                <PLUGIN src="custombutton" MenuOffset="10" buttons="Btn1,Btn3,Btn2" Btn1.Url="javascript: void printImage('$$URLView$$')" Btn1.Tooltip="Print Current View" Btn1.LabelFrame="7" Btn3.Url="javascript:void saveImage('$$URLView$$');" Btn3.Tooltip="Download image" Btn3.LabelFrame="6" Btn2.Url="javascript:void saveToImageGroup('$$View$$','$$selection$$','$$URLView$$');" Btn2.Tooltip="Save view to image group" Btn2.LabelFrame="8" />
<!--                <plugin src="SelectFrame" Visible="false" Window="false" rotate="1" AspectRatio="1:5" events="true" callback="onSelect" initialvalue="1,1,0,0
,0.25,0.25,0" >
                </plugin>-->
        <!--    <PLUGIN src="hotspots" visible="false">
                  <HotSpots>
                     <rect spot="1, 1, 0.20686119, 0.61174863, 0.27701569, 0.75000013, 0" tip="rect" view="1, 1, 0.174354, 0.630768, 0.299354, 0.755768, 0"/>
                  </HotSpots>
                </PLUGIN> -->

        </PLUGINS>

        <Options>
                <FSIBase value="config/" />
                <MenuAlign value="BR" />
                <Language value="english" />
                <ScenePreload value="true" />
                <AnimationSpeed value="80" />
                <Animation value="BEST" />              
    <HelpURL value="html/help_en.html#fsi" />
                <HelpURLTarget value="erez_help" />
                <ClockProgress_PosX value="C" />
                <ClockProgress_PosY value="C" />
                <skin value="artstor" />
                <intro value="intro_artstor" />

                <!-- Custom Tool Tips -->
                <Language value="artstor/english" />


                <MenuAlign value="br" />

                <!-- hide the Hide/Show UI button -->
                <UISwitchable value="0" />

                <!-- Special Custom Parameters below -->
                <LogoURL value="http://www.artstor.org/" />
                <LogoURLTarget value="_blank" />
                <LogoTip value="Enter ARTstor" />

                <TermsURL value="http://www.artstor.org/info/about/terms_conditions.jsp" />
                <TermsURLTarget value="_blank" />
                <TermsTip value="Terms & Conditions" />
                <Terms value="0" />

                <AutoZoom value="100" />

        </Options>

</fsi_parameter>
