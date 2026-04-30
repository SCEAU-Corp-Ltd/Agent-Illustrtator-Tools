# Illustrator Menu Command Links

This index is generated from `data/illustrator-menu-commands.csv`,
which mirrors the public AiCommandPalette menu command data.

Use the `value` field as the command identifier when an Illustrator
automation surface supports menu-command execution. Verify each command
against the active Illustrator version before using it in a destructive
or batch workflow.

Source: https://github.com/joshbduncan/AiCommandPalette/blob/main/data/menu_commands.csv

Total command rows: 786.

## Groups

| Group | Rows |
|---|---:|
| [About](#about) | 1 |
| [Edit](#edit) | 38 |
| [Effect](#effect) | 119 |
| [File](#file) | 26 |
| [Help](#help) | 10 |
| [Object](#object) | 146 |
| [Other](#other) | 2 |
| [Other Misc](#other-misc) | 14 |
| [Other Object](#other-object) | 6 |
| [Other Text](#other-text) | 26 |
| [Palette](#palette) | 9 |
| [Preferences](#preferences) | 15 |
| [Select](#select) | 39 |
| [Type](#type) | 47 |
| [View](#view) | 50 |
| [Window](#window) | 238 |

## About

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1703 | `about` | About Illustrator... |  |  |  |

## Edit

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1026 | `undo` | Edit > Undo | document |  |  |
| menu_1027 | `redo` | Edit > Redo | document |  |  |
| menu_1028 | `cut` | Edit > Cut | document, selection |  |  |
| menu_1029 | `copy` | Edit > Copy | document, selection |  |  |
| menu_1030 | `paste` | Edit > Paste | document |  |  |
| menu_1031 | `pasteFront` | Edit > Paste in Front | document |  |  |
| menu_1032 | `pasteBack` | Edit > Paste in Back | document |  |  |
| menu_1033 | `pasteInPlace` | Edit > Paste in Place | document |  |  |
| menu_1034 | `pasteInAllArtboard` | Edit > Paste on All Artboards | document |  |  |
| menu_1035 | `pasteWithoutFormatting` | Edit > Paste without Formatting | document | >= 25.3 |  |
| menu_1036 | `clear` | Edit > Clear | document, selection |  |  |
| menu_1037 | `Find and Replace` | Edit > Find & Replace... | document |  |  |
| menu_1038 | `Find Next` | Edit > Find Next | document |  |  |
| menu_1039 | `Auto Spell Check` | Edit > Spelling > Auto Spell Check |  | >= 24 |  |
| menu_1040 | `Check Spelling` | Edit > Spelling > Check Spelling... | document | >= 24 |  |
| menu_1041 | `Edit Custom Dictionary...` | Edit > Edit Custom Dictionary... | document |  |  |
| menu_1042 | `Recolor Art Dialog` | Edit > Edit Colors > Recolor Artwork... | document, selection |  |  |
| menu_1043 | `Adjust3` | Edit > Edit Colors > Adjust Color Balance... | document, selection |  |  |
| menu_1044 | `Colors3` | Edit > Edit Colors > Blend Front to Back | document, selection |  |  |
| menu_1045 | `Colors4` | Edit > Edit Colors > Blend Horizontally | document, selection |  |  |
| menu_1046 | `Colors5` | Edit > Edit Colors > Blend Vertically | document, selection |  |  |
| menu_1047 | `Colors8` | Edit > Edit Colors > Convert to CMYK | document, selection |  |  |
| menu_1048 | `Colors7` | Edit > Edit Colors > Convert to Grayscale | document, selection |  |  |
| menu_1049 | `Colors9` | Edit > Edit Colors > Convert to RGB | document, selection |  |  |
| menu_1050 | `Generative Recolor Art Dialog` | Edit > Edit Colors > Generative Recolor | document, selection | >= 27.6 |  |
| menu_1051 | `Colors6` | Edit > Edit Colors > Invert Colors | document, selection |  |  |
| menu_1052 | `Overprint2` | Edit > Edit Colors > Overprint Black... | document, selection |  |  |
| menu_1053 | `Saturate3` | Edit > Edit Colors > Saturate... | document, selection |  |  |
| menu_1054 | `EditOriginal Menu Item` | Edit > Edit Original | document, selection |  |  |
| menu_1055 | `Transparency Presets` | Edit > Transparency Flattener Presets... |  |  |  |
| menu_1056 | `Print Presets` | Edit > Print Presets... |  |  |  |
| menu_1057 | `PDF Presets` | Edit > Adobe PDF Presets... |  |  |  |
| menu_1058 | `PerspectiveGridPresets` | Edit > Perspective Grid Presets... |  |  |  |
| menu_1059 | `color` | Edit > Color Settings... |  |  |  |
| menu_1060 | `assignprofile` | Edit > Assign Profile... | document |  |  |
| menu_1061 | `KBSC Menu Item` | Edit > Keyboard Shortcuts... |  |  |  |
| menu_1062 | `SWFPresets` | Edit > SWF Presets... |  | 22-25.9 |  |
| menu_1063 | `TouchPref` | Edit > Preferences > Touch Workspace |  |  | ignored |

## Effect

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1277 | `Adobe Apply Last Effect` | Effect > Apply Last Effect | document |  |  |
| menu_1278 | `Adobe Last Effect` | Effect > Last Effect | document |  |  |
| menu_1279 | `Live Rasterize Effect Setting` | Effect > Document Raster Effects Settings... | document |  |  |
| menu_1280 | `Live Adobe Geometry3D Extrude` | Effect > 3D and Materials > Extrude & Bevel... | document | >= 26 |  |
| menu_1281 | `Live Adobe Geometry3D Revolve` | Effect > 3D and Materials > Revolve... | document | >= 26 |  |
| menu_1282 | `Live Adobe Geometry3D Inflate` | Effect > 3D and Materials > Inflate... | document | >= 26 |  |
| menu_1283 | `Live Adobe Geometry3D Rotate` | Effect > 3D and Materials > Rotate... | document | >= 26 |  |
| menu_1284 | `Live Adobe Geometry3D Materials` | Effect > 3D and Materials > Materials... | document | >= 26 |  |
| menu_1285 | `Live 3DExtrude` | Effect > 3D and Materials > 3D (Classic) > Extrude & Bevel (Classic)... | document | >= 26 |  |
| menu_1286 | `Live 3DRevolve` | Effect > 3D and Materials > 3D (Classic) > Revolve (Classic)... | document | >= 26 |  |
| menu_1287 | `Live 3DRotate` | Effect > 3D and Materials > 3D (Classic) > Rotate (Classic)... | document | >= 26 |  |
| menu_1288 | `Live Rectangle` | Effect > Convert to Shape > Rectangle... | document |  |  |
| menu_1289 | `Live Rounded Rectangle` | Effect > Convert to Shape > Rounded Rectangle... | document |  |  |
| menu_1290 | `Live Ellipse` | Effect > Convert to Shape > Ellipse... | document |  |  |
| menu_1291 | `Live Trim Marks` | Effect > Crop Marks | document |  |  |
| menu_1292 | `Live Free Distort` | Effect > Distort & Transform > Free Distort... | document |  |  |
| menu_1293 | `Live Pucker & Bloat` | Effect > Distort & Transform > Pucker & Bloat... | document |  |  |
| menu_1294 | `Live Roughen` | Effect > Distort & Transform > Roughen... | document |  |  |
| menu_1295 | `Live Transform` | Effect > Distort & Transform > Transform... | document |  |  |
| menu_1296 | `Live Scribble and Tweak` | Effect > Distort & Transform > Tweak... | document |  |  |
| menu_1297 | `Live Twist` | Effect > Distort & Transform > Twist... | document |  |  |
| menu_1298 | `Live Zig Zag` | Effect > Distort & Transform > Zig Zag... | document |  |  |
| menu_1299 | `Live Offset Path` | Effect > Path > Offset Path... | document |  |  |
| menu_1300 | `Live Outline Object` | Effect > Path > Outline Object | document |  |  |
| menu_1301 | `Live Outline Stroke` | Effect > Path > Outline Stroke | document |  |  |
| menu_1302 | `Live Pathfinder Add` | Effect > Pathfinder > Add | document |  |  |
| menu_1303 | `Live Pathfinder Intersect` | Effect > Pathfinder > Intersect | document |  |  |
| menu_1304 | `Live Pathfinder Exclude` | Effect > Pathfinder > Exclude | document |  |  |
| menu_1305 | `Live Pathfinder Subtract` | Effect > Pathfinder > Subtract | document |  |  |
| menu_1306 | `Live Pathfinder Minus Back` | Effect > Pathfinder > Minus Back | document |  |  |
| menu_1307 | `Live Pathfinder Divide` | Effect > Pathfinder > Divide | document |  |  |
| menu_1308 | `Live Pathfinder Trim` | Effect > Pathfinder > Trim | document |  |  |
| menu_1309 | `Live Pathfinder Merge` | Effect > Pathfinder > Merge | document |  |  |
| menu_1310 | `Live Pathfinder Crop` | Effect > Pathfinder > Crop | document |  |  |
| menu_1311 | `Live Pathfinder Outline` | Effect > Pathfinder > Outline | document |  |  |
| menu_1312 | `Live Pathfinder Hard Mix` | Effect > Pathfinder > Hard Mix | document |  |  |
| menu_1313 | `Live Pathfinder Soft Mix` | Effect > Pathfinder > Soft Mix... | document |  |  |
| menu_1314 | `Live Pathfinder Trap` | Effect > Pathfinder > Trap... | document |  |  |
| menu_1315 | `Live Rasterize` | Effect > Rasterize... | document |  |  |
| menu_1316 | `Live Adobe Drop Shadow` | Effect > Stylize > Drop Shadow... | document |  |  |
| menu_1317 | `Live Feather` | Effect > Stylize > Feather... | document |  |  |
| menu_1318 | `Live Inner Glow` | Effect > Stylize > Inner Glow... | document |  |  |
| menu_1319 | `Live Outer Glow` | Effect > Stylize > Outer Glow... | document |  |  |
| menu_1320 | `Live Adobe Round Corners` | Effect > Stylize > Round Corners... | document |  |  |
| menu_1321 | `Live Scribble Fill` | Effect > Stylize > Scribble... | document |  |  |
| menu_1322 | `Live SVG Filters` | Effect > SVG Filters > Apply SVG Filter... | document |  |  |
| menu_1323 | `SVG Filter Import` | Effect > SVG Filters > Import SVG Filter... | document |  |  |
| menu_1324 | `Live Deform Arc` | Effect > Warp > Arc... | document |  |  |
| menu_1325 | `Live Deform Arc Lower` | Effect > Warp > Arc Lower... | document |  |  |
| menu_1326 | `Live Deform Arc Upper` | Effect > Warp > Arc Upper... | document |  |  |
| menu_1327 | `Live Deform Arch` | Effect > Warp > Arch... | document |  |  |
| menu_1328 | `Live Deform Bulge` | Effect > Warp > Bulge... | document |  |  |
| menu_1329 | `Live Deform Shell Lower` | Effect > Warp > Shell Lower... | document |  |  |
| menu_1330 | `Live Deform Shell Upper` | Effect > Warp > Shell Upper... | document |  |  |
| menu_1331 | `Live Deform Flag` | Effect > Warp > Flag... | document |  |  |
| menu_1332 | `Live Deform Wave` | Effect > Warp > Wave... | document |  |  |
| menu_1333 | `Live Deform Fish` | Effect > Warp > Fish... | document |  |  |
| menu_1334 | `Live Deform Rise` | Effect > Warp > Rise... | document |  |  |
| menu_1335 | `Live Deform Fisheye` | Effect > Warp > Fisheye... | document |  |  |
| menu_1336 | `Live Deform Inflate` | Effect > Warp > Inflate... | document |  |  |
| menu_1337 | `Live Deform Squeeze` | Effect > Warp > Squeeze... | document |  |  |
| menu_1338 | `Live Deform Twist` | Effect > Warp > Twist... | document |  |  |
| menu_1339 | `Live PSAdapter_plugin_GEfc` | Effect > Effect Gallery... | document |  |  |
| menu_1340 | `Live PSAdapter_plugin_ClrP` | Effect > Artistic > Colored Pencil... | document |  |  |
| menu_1341 | `Live PSAdapter_plugin_Ct` | Effect > Artistic > Cutout... | document |  |  |
| menu_1342 | `Live PSAdapter_plugin_DryB` | Effect > Artistic > Dry Brush... | document |  |  |
| menu_1343 | `Live PSAdapter_plugin_FlmG` | Effect > Artistic > Film Grain... | document |  |  |
| menu_1344 | `Live PSAdapter_plugin_Frsc` | Effect > Artistic > Fresco... | document |  |  |
| menu_1345 | `Live PSAdapter_plugin_NGlw` | Effect > Artistic > Neon Glow... | document |  |  |
| menu_1346 | `Live PSAdapter_plugin_PntD` | Effect > Artistic > Paint Daubs... | document |  |  |
| menu_1347 | `Live PSAdapter_plugin_PltK` | Effect > Artistic > Palette Knife... | document |  |  |
| menu_1348 | `Live PSAdapter_plugin_PlsW` | Effect > Artistic > Plastic Wrap... | document |  |  |
| menu_1349 | `Live PSAdapter_plugin_PstE` | Effect > Artistic > Poster Edges... | document |  |  |
| menu_1350 | `Live PSAdapter_plugin_RghP` | Effect > Artistic > Rough Pastels... | document |  |  |
| menu_1351 | `Live PSAdapter_plugin_SmdS` | Effect > Artistic > Smudge Stick... | document |  |  |
| menu_1352 | `Live PSAdapter_plugin_Spng` | Effect > Artistic > Sponge... | document |  |  |
| menu_1353 | `Live PSAdapter_plugin_Undr` | Effect > Artistic > Underpainting... | document |  |  |
| menu_1354 | `Live PSAdapter_plugin_Wtrc` | Effect > Artistic > Watercolor... | document |  |  |
| menu_1355 | `Live Adobe PSL Gaussian Blur` | Effect > Blur > Gaussian Blur... | document |  |  |
| menu_1356 | `Live PSAdapter_plugin_RdlB` | Effect > Blur > Radial Blur... | document |  |  |
| menu_1357 | `Live PSAdapter_plugin_SmrB` | Effect > Blur > Smart Blur... | document |  |  |
| menu_1358 | `Live PSAdapter_plugin_AccE` | Effect > Brush Strokes > Accented Edges... | document |  |  |
| menu_1359 | `Live PSAdapter_plugin_AngS` | Effect > Brush Strokes > Angled Strokes... | document |  |  |
| menu_1360 | `Live PSAdapter_plugin_Crsh` | Effect > Brush Strokes > Crosshatch... | document |  |  |
| menu_1361 | `Live PSAdapter_plugin_DrkS` | Effect > Brush Strokes > Dark Strokes... | document |  |  |
| menu_1362 | `Live PSAdapter_plugin_InkO` | Effect > Brush Strokes > Ink Outlines... | document |  |  |
| menu_1363 | `Live PSAdapter_plugin_Spt` | Effect > Brush Strokes > Spatter... | document |  |  |
| menu_1364 | `Live PSAdapter_plugin_SprS` | Effect > Brush Strokes > Sprayed Strokes... | document |  |  |
| menu_1365 | `Live PSAdapter_plugin_Smie` | Effect > Brush Strokes > Sumi-e... | document |  |  |
| menu_1366 | `Live PSAdapter_plugin_DfsG` | Effect > Distort > Diffuse Glow... | document |  |  |
| menu_1367 | `Live PSAdapter_plugin_Gls` | Effect > Distort > Glass... | document |  |  |
| menu_1368 | `Live PSAdapter_plugin_OcnR` | Effect > Distort > Ocean Ripple... | document |  |  |
| menu_1369 | `Live PSAdapter_plugin_ClrH` | Effect > Pixelate > Color Halftone... | document |  |  |
| menu_1370 | `Live PSAdapter_plugin_Crst` | Effect > Pixelate > Crystallize... | document |  |  |
| menu_1371 | `Live PSAdapter_plugin_Mztn` | Effect > Pixelate > Mezzotint... | document |  |  |
| menu_1372 | `Live PSAdapter_plugin_Pntl` | Effect > Pixelate > Pointillize... | document |  |  |
| menu_1373 | `Live PSAdapter_plugin_BsRl` | Effect > Sketch > Bas Relief... | document |  |  |
| menu_1374 | `Live PSAdapter_plugin_ChlC` | Effect > Sketch > Chalk & Charcoal... | document |  |  |
| menu_1375 | `Live PSAdapter_plugin_Chrc` | Effect > Sketch > Charcoal... | document |  |  |
| menu_1376 | `Live PSAdapter_plugin_Chrm` | Effect > Sketch > Chrome... | document |  |  |
| menu_1377 | `Live PSAdapter_plugin_CntC` | Effect > Sketch > Conté Crayon... | document |  |  |
| menu_1378 | `Live PSAdapter_plugin_GraP` | Effect > Sketch > Graphic Pen... | document |  |  |
| menu_1379 | `Live PSAdapter_plugin_HlfS` | Effect > Sketch > Halftone Pattern... | document |  |  |
| menu_1380 | `Live PSAdapter_plugin_NtPr` | Effect > Sketch > Note Paper... | document |  |  |
| menu_1381 | `Live PSAdapter_plugin_Phtc` | Effect > Sketch > Photocopy... | document |  |  |
| menu_1382 | `Live PSAdapter_plugin_Plst` | Effect > Sketch > Plaster... | document |  |  |
| menu_1383 | `Live PSAdapter_plugin_Rtcl` | Effect > Sketch > Reticulation... | document |  |  |
| menu_1384 | `Live PSAdapter_plugin_Stmp` | Effect > Sketch > Stamp... | document |  |  |
| menu_1385 | `Live PSAdapter_plugin_TrnE` | Effect > Sketch > Torn Edges... | document |  |  |
| menu_1386 | `Live PSAdapter_plugin_WtrP` | Effect > Sketch > Water Paper... | document |  |  |
| menu_1387 | `Live PSAdapter_plugin_GlwE` | Effect > Stylize > Glowing Edges... | document |  |  |
| menu_1388 | `Live PSAdapter_plugin_Crql` | Effect > Texture > Craquelure... | document |  |  |
| menu_1389 | `Live PSAdapter_plugin_Grn` | Effect > Texture > Grain... | document |  |  |
| menu_1390 | `Live PSAdapter_plugin_MscT` | Effect > Texture > Mosaic Tiles... | document |  |  |
| menu_1391 | `Live PSAdapter_plugin_Ptch` | Effect > Texture > Patchwork... | document |  |  |
| menu_1392 | `Live PSAdapter_plugin_StnG` | Effect > Texture > Stained Glass... | document |  |  |
| menu_1393 | `Live PSAdapter_plugin_Txtz` | Effect > Texture > Texturizer... | document |  |  |
| menu_1394 | `Live PSAdapter_plugin_Dntr` | Effect > Video > De-Interlace... | document |  |  |
| menu_1395 | `Live PSAdapter_plugin_NTSC` | Effect > Video > NTSC Colors | document |  |  |

## File

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1000 | `new` | File > New... |  |  |  |
| menu_1001 | `newFromTemplate` | File > New from Template... |  |  |  |
| menu_1002 | `open` | File > Open... |  |  |  |
| menu_1003 | `Adobe Bridge Browse` | File > Browse in Bridge... |  |  |  |
| menu_1004 | `close` | File > Close | document |  |  |
| menu_1005 | `save` | File > Save | document |  |  |
| menu_1006 | `saveas` | File > Save As... | document |  |  |
| menu_1007 | `saveacopy` | File > Save a Copy... | document |  |  |
| menu_1008 | `saveastemplate` | File > Save as Template... | document |  |  |
| menu_1009 | `Adobe AI Save Selected Slices` | File > Save Selected Slices... | document, selection |  |  |
| menu_1010 | `revert` | File > Revert | document |  |  |
| menu_1011 | `Search Adobe Stock` | File > Search Adobe Stock |  | >= 19 |  |
| menu_1012 | `AI Place` | File > Place... | document |  |  |
| menu_1013 | `Generate Modal File Menu` | File > Generate Vectors... | document | 28.6-29.999 | Note that there is a space after 'Menu' |
| menu_1014 | `exportForScreens` | File > Export > Export For Screens... | document | >= 20 |  |
| menu_1015 | `export` | File > Export > Export As... | document |  |  |
| menu_1016 | `Adobe AI Save For Web` | File > Export > Save for Web (Legacy)... | document |  |  |
| menu_1017 | `exportSelection` | File > Export Selection... | document | >= 20 |  |
| menu_1018 | `Package Menu Item` | File > Package | document |  |  |
| menu_1019 | `ai_browse_for_script` | File > Scripts > Other Script... |  |  |  |
| menu_1020 | `document` | File > Document Setup... | document |  | ignored |
| menu_1021 | `doc-color-cmyk` | File > Document Color Mode > CMYK Color | document |  |  |
| menu_1022 | `doc-color-rgb` | File > Document Color Mode > RGB Color | document |  |  |
| menu_1023 | `File Info` | File > File Info... | document |  |  |
| menu_1024 | `Print` | File > Print... | document |  |  |
| menu_1025 | `quit` | File > Exit |  |  |  |

## Help

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1684 | `helpcontent` | Help > Illustrator Help... |  |  |  |
| menu_1685 | `whatsNewContent` | Help > Tutorials... |  | >= 27.9 |  |
| menu_1686 | `supportCommunity` | Help > Support Community |  | >= 26 |  |
| menu_1687 | `wishform` | Help > Submit Bug/Feature Request... |  | >= 25 |  |
| menu_1688 | `System Info` | Help > System Info... |  |  |  |
| menu_1689 | `_GenericPluginMenuItem 1` | Help > Manage My Account... |  |  | ignored; These seem to correspond to different menu items depending on Ai version and installed plug-ins. Number at the end may also be off by 1 as well. |
| menu_1690 | `_GenericPluginMenuItem 2` | Help > Manage My Account... |  |  | ignored; These seem to correspond to different menu items depending on Ai version and installed plug-ins. Number at the end may also be off by 1 as well. |
| menu_1691 | `_GenericPluginMenuItem 3` | Help > Sign In... / Sign Out... |  |  | ignored; These seem to correspond to different menu items depending on Ai version and installed plug-ins. Number at the end may also be off by 1 as well. |
| menu_1692 | `_GenericPluginMenuItem 4` | Help > Updates... |  |  | ignored; These seem to correspond to different menu items depending on Ai version and installed plug-ins. Number at the end may also be off by 1 as well. |
| menu_1693 | `Help Menu Beta log file` | Help > Beta log file |  |  | ignored |

## Object

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1064 | `transformagain` | Object > Transform > Transform Again | document, selection |  |  |
| menu_1065 | `transformmove` | Object > Transform > Move... | document, selection |  |  |
| menu_1066 | `transformrotate` | Object > Transform > Rotate... | document, selection |  |  |
| menu_1067 | `transformreflect` | Object > Transform > Reflect... | document, selection |  |  |
| menu_1068 | `transformscale` | Object > Transform > Scale... | document, selection |  |  |
| menu_1069 | `transformshear` | Object > Transform > Shear... | document, selection |  |  |
| menu_1070 | `Transform v23` | Object > Transform Each... | document, selection |  |  |
| menu_1071 | `AI Reset Bounding Box` | Object > Transform > Reset Bounding Box | document, selection |  |  |
| menu_1072 | `sendToFront` | Object > Arrange > Bring to Front | document, selection |  |  |
| menu_1073 | `sendForward` | Object > Arrange > Bring Forward | document, selection |  |  |
| menu_1074 | `sendBackward` | Object > Arrange > Send Backward | document, selection |  |  |
| menu_1075 | `sendToBack` | Object > Arrange > Send to Back | document, selection |  |  |
| menu_1076 | `Selection Hat 2` | Object > Arrange > Send to Current Layer | document, selection |  |  |
| menu_1077 | `Horizontal Align Left` | Object > Align > Horizontal Align Left | document | >= 24 |  |
| menu_1078 | `Horizontal Align Center` | Object > Align > Horizontal Align Center | document | >= 24 |  |
| menu_1079 | `Horizontal Align Right` | Object > Align > Horizontal Align Right | document | >= 24 |  |
| menu_1080 | `Vertical Align Top` | Object > Align > Vertical Align Top | document | >= 24 |  |
| menu_1081 | `Vertical Align Center` | Object > Align > Vertical Align Center | document | >= 24 |  |
| menu_1082 | `Vertical Align Bottom` | Object > Align > Vertical Align Bottom | document | >= 24 |  |
| menu_1083 | `Vertical Distribute Top` | Object > Distribute > Vertical Distribute Top | document, selection | >= 27 |  |
| menu_1084 | `Vertical Distribute Center` | Object > Distribute > Vertical Distribute Center | document, selection | >= 27 |  |
| menu_1085 | `Vertical Distribute Bottom` | Object > Distribute > Vertical Distribute Bottom | document, selection | >= 27 |  |
| menu_1086 | `Horizontal Distribute Left` | Object > Distribute > Horizontal Distribute Left | document, selection | >= 27 |  |
| menu_1087 | `Horizontal Distribute Center` | Object > Distribute > Horizontal Distribute Center | document, selection | >= 27 |  |
| menu_1088 | `Horizontal Distribute Right` | Object > Distribute > Horizontal Distribute Right | document, selection | >= 27 |  |
| menu_1089 | `group` | Object > Group | document, selection |  |  |
| menu_1090 | `ungroup` | Object > Ungroup | document, selection |  |  |
| menu_1091 | `ungroup all` | Object > Ungroup All | document, selection | >= 29.3 |  |
| menu_1092 | `lock` | Object > Lock > Selection | document, selection |  |  |
| menu_1093 | `Selection Hat 5` | Object > Lock > All Artwork Above | document, selection |  |  |
| menu_1094 | `Selection Hat 7` | Object > Lock > Other Layers | document, selection |  |  |
| menu_1095 | `unlockAll` | Object > Unlock All | document |  |  |
| menu_1096 | `hide` | Object > Hide > Selection | document, selection |  |  |
| menu_1097 | `Selection Hat 4` | Object > Hide > All Artwork Above | document, selection |  |  |
| menu_1098 | `Selection Hat 6` | Object > Hide > Other Layers | document, selection |  |  |
| menu_1099 | `showAll` | Object > Show All | document |  |  |
| menu_1100 | `Crop Image` | Object > Crop Image | document, selection | >= 23 |  |
| menu_1101 | `Rasterize 8 menu item` | Object > Rasterize... | document, selection |  |  |
| menu_1102 | `make mesh` | Object > Create Gradient Mesh... | document, selection |  |  |
| menu_1103 | `AI Object Mosaic Plug-in4` | Object > Create Object Mosaic... | document, selection |  |  |
| menu_1104 | `TrimMark v25` | Object > Create Trim Marks... | document, selection |  |  |
| menu_1105 | `Flatten Transparency` | Object > Flatten Transparency... | document, selection |  |  |
| menu_1106 | `Make Pixel Perfect` | Object > Make Pixel Perfect | document, selection |  |  |
| menu_1107 | `GenAIConsolidatedGenerateVectors` | Object > Generative > Generate Vectors... | document, selection | >= 30.0 | Moved to Generative submenu in v30.0, Changed from 'Generate Modal File Menu ' at v30.0 |
| menu_1108 | `GenAIConsolidatedShapeFill` | Object > Generative > Gen Shape Fill... | document, selection | >= 30.0 | Moved to Generative submenu in v30.0, Changed from 'Shape Fill Object Menu' at v30.0 |
| menu_1109 | `Gen Expand Object Make` | Object > Generative > Generative Expand... > Make... | document | >= 30.0 |  |
| menu_1110 | `Gen Expand Object Combine` | Object > Generative > Generative Expand... > Combine | document | >= 30.0 |  |
| menu_1111 | `GenAIConsolidatedBleed` | Object > Generative > Print Bleed... | document, selection | >= 30.0 | Moved to Generative submenu in v30.0, Changed from 'Shape Fill Object Menu' at v30.0 |
| menu_1112 | `GenAIConsolidatedRecolor` | Object > Generative > Generative Recolor... | document, selection | >= 30.0 |  |
| menu_1113 | `GenAIConsolidatedPatterns` | Object > Generative > Generate Patterns... | document, selection | >= 30.0 | Moved to Generative submenu in v30.0, Changed from 'Adobe Generative Patterns Panel' at v30.0 |
| menu_1114 | `GenAIConsolidatedVariations` | Object > Generative > Generation History... | document, selection | >= 30.0 |  |
| menu_1115 | `AISlice Make Slice` | Object > Slice > Make | document, selection |  |  |
| menu_1116 | `AISlice Release Slice` | Object > Slice > Release | document, selection |  |  |
| menu_1117 | `AISlice Create from Guides` | Object > Slice > Create from Guides | document |  |  |
| menu_1118 | `AISlice Create from Selection` | Object > Slice > Create from Selection | document, selection |  |  |
| menu_1119 | `AISlice Duplicate` | Object > Slice > Duplicate Slice | document, selection |  |  |
| menu_1120 | `AISlice Combine` | Object > Slice > Combine Slices | document, selection |  |  |
| menu_1121 | `AISlice Divide` | Object > Slice > Divide Slices... | document, selection |  |  |
| menu_1122 | `AISlice Delete All Slices` | Object > Slice > Delete All | document, selection |  |  |
| menu_1123 | `AISlice Slice Options` | Object > Slice > Slice Options... | document, selection |  |  |
| menu_1124 | `AISlice Clip to Artboard` | Object > Slice > Clip to Artboard | document, selection |  |  |
| menu_1125 | `Generate Modal File Menu` | Object > Generate Vectors... | document | 28.6-29.999 | Note that there is a space after 'Menu' |
| menu_1126 | `Expand3` | Object > Expand... | document, selection |  |  |
| menu_1127 | `expandStyle` | Object > Expand Appearance | document, selection |  |  |
| menu_1128 | `join` | Object > Path > Join | document, selection |  |  |
| menu_1129 | `average` | Object > Path > Average... | document, selection |  |  |
| menu_1130 | `OffsetPath v22` | Object > Path > Outline Stroke | document, selection |  |  |
| menu_1131 | `OffsetPath v23` | Object > Path > Offset Path... | document, selection |  |  |
| menu_1132 | `Reverse Path Direction` | Object > Path > Reverse Path Direction | document, selection | >= 21 |  |
| menu_1133 | `simplify menu item` | Object > Path > Simplify... | document, selection |  |  |
| menu_1134 | `Add Anchor Points2` | Object > Path > Add Anchor Points | document, selection |  |  |
| menu_1135 | `Remove Anchor Points menu` | Object > Path > Remove Anchor Points | document, selection |  |  |
| menu_1136 | `Knife Tool2` | Object > Path > Divide Objects Below | document, selection |  |  |
| menu_1137 | `Rows and Columns....` | Object > Path > Split Into Grid... | document, selection |  |  |
| menu_1138 | `cleanup menu item` | Object > Path > Clean Up... | document |  |  |
| menu_1139 | `smooth menu item` | Object > Path > Smooth | document, selection | >= 28 |  |
| menu_1140 | `Convert to Shape` | Object > Shape > Convert to Shapes | document, selection | >= 18 |  |
| menu_1141 | `Expand Shape` | Object > Shape > Expand Shapes | document, selection | >= 18 |  |
| menu_1142 | `Shape Fill Object Menu` | Object > Gen Shape Fill... | document, selection | 28.6-29.999 |  |
| menu_1143 | `Gen Expand Object Make` | Object > Generative Expand... > Make... | document, selection | 29.6-29.999 |  |
| menu_1144 | `Gen Expand Object Combine` | Object > Generative Expand... > Combine | document, selection | 29.6-29.999 |  |
| menu_1145 | `Gen Bleed Object Menu` | Object > Print Bleed... | document, selection | 29.6-29.999 |  |
| menu_1146 | `Adobe Make Pattern` | Object > Pattern > Make | document |  |  |
| menu_1147 | `Adobe Edit Pattern` | Object > Pattern > Edit Pattern | document, selection |  |  |
| menu_1148 | `Adobe Pattern Tile Color` | Object > Pattern > Tile Edge Color... |  |  |  |
| menu_1149 | `Adobe Generative Patterns Panel` | Object > Pattern > Generate Patterns | document | 28.6-29.999 |  |
| menu_1150 | `GenAIConsolidatedPatterns` | Object > Pattern > Generate Patterns | document | >= 30.0 |  |
| menu_1151 | `Partial Rearrange Make` | Object > Intertwine > Make | document, selection | >= 27 |  |
| menu_1152 | `Partial Rearrange Release` | Object > Intertwine > Release | document, selection | >= 27 |  |
| menu_1153 | `Partial Rearrange Edit` | Object > Intertwine > Edit | document, selection | >= 27 |  |
| menu_1154 | `Make Radial Repeat` | Object > Repeat > Make Radial | document, selection | >= 25.1 |  |
| menu_1155 | `Make Grid Repeat` | Object > Repeat > Make Grid | document, selection | >= 25.1 |  |
| menu_1156 | `Make Symmetry Repeat` | Object > Repeat > Make Symmetry | document, selection | >= 25.1 |  |
| menu_1157 | `Release Repeat Art` | Object > Repeat > Release | document, selection | >= 25.1 |  |
| menu_1158 | `Repeat Art Options` | Object > Repeat > Repeat Options... | document | >= 25.1 |  |
| menu_1159 | `Attach Objects on Path` | Object > Objects on Path > Attach... | document, selection | >= 29 |  |
| menu_1160 | `Options Objects on Path` | Object > Objects on Path > Options... | document, selection | >= 29 |  |
| menu_1161 | `Expand Objects on Path` | Object > Objects on Path > Expand | document, selection | >= 29 |  |
| menu_1162 | `Path Blend Make` | Object > Blend > Make | document, selection |  |  |
| menu_1163 | `Path Blend Release` | Object > Blend > Release | document, selection |  |  |
| menu_1164 | `Path Blend Options` | Object > Blend > Blend Options... |  |  |  |
| menu_1165 | `Path Blend Expand` | Object > Blend > Expand | document, selection |  |  |
| menu_1166 | `Path Blend Replace Spine` | Object > Blend > Replace Spine | document, selection |  |  |
| menu_1167 | `Path Blend Reverse Spine` | Object > Blend > Reverse Spine | document, selection |  |  |
| menu_1168 | `Path Blend Reverse Stack` | Object > Blend > Reverse Front to Back | document, selection |  |  |
| menu_1169 | `Make Warp` | Object > Envelope Distort > Make with Warp... | document, selection |  |  |
| menu_1170 | `Create Envelope Grid` | Object > Envelope Distort > Make with Mesh... | document, selection |  |  |
| menu_1171 | `Make Envelope` | Object > Envelope Distort > Make with Top Object | document, selection |  |  |
| menu_1172 | `Release Envelope` | Object > Envelope Distort > Release | document, selection |  |  |
| menu_1173 | `Envelope Options` | Object > Envelope Distort > Envelope Options... |  |  |  |
| menu_1174 | `Expand Envelope` | Object > Envelope Distort > Expand | document, selection |  |  |
| menu_1175 | `Edit Envelope Contents` | Object > Envelope Distort > Edit Contents | document, selection |  |  |
| menu_1176 | `Attach to Active Plane` | Object > Perspective > Attach to Active Plane | document, selection |  |  |
| menu_1177 | `Release with Perspective` | Object > Perspective > Release with Perspective | document, selection |  |  |
| menu_1178 | `Show Object Grid Plane` | Object > Perspective > Move Plane to Match Object | document, selection |  |  |
| menu_1179 | `Edit Original Object` | Object > Perspective > Edit Text | document, selection |  |  |
| menu_1180 | `Make Planet X` | Object > Live Paint > Make | document, selection |  |  |
| menu_1181 | `Marge Planet X` | Object > Live Paint > Merge | document, selection |  |  |
| menu_1182 | `Release Planet X` | Object > Live Paint > Release | document, selection |  |  |
| menu_1183 | `Planet X Options` | Object > Live Paint > Gap Options... |  |  |  |
| menu_1184 | `Expand Planet X` | Object > Live Paint > Expand | document, selection |  |  |
| menu_1185 | `Make Image Tracing` | Object > Image Trace > Make | document, selection |  |  |
| menu_1186 | `Make and Expand Image Tracing` | Object > Image Trace > Make and Expand | document, selection |  |  |
| menu_1187 | `Release Image Tracing` | Object > Image Trace > Release | document, selection |  |  |
| menu_1188 | `Expand Image Tracing` | Object > Image Trace > Expand | document, selection |  |  |
| menu_1189 | `Make Vector Edge` | Object > Mockup > Make | document, selection | >= 28 |  |
| menu_1190 | `Release Vector Edge` | Object > Mockup > Release | document, selection | >= 28 |  |
| menu_1191 | `Edit Vector Edge` | Object > Mockup > Edit | document, selection | >= 28 |  |
| menu_1192 | `Make Text Wrap` | Object > Text Wrap > Make | document, selection |  |  |
| menu_1193 | `Release Text Wrap` | Object > Text Wrap > Release | document, selection |  |  |
| menu_1194 | `Text Wrap Options...` | Object > Text Wrap > Text Wrap Options... |  |  |  |
| menu_1195 | `makeMask` | Object > Clipping Mask > Make | document, selection |  |  |
| menu_1196 | `releaseMask` | Object > Clipping Mask > Release | document, selection |  |  |
| menu_1197 | `editMask` | Object > Clipping Mask > Edit Mask | document, selection |  |  |
| menu_1198 | `compoundPath` | Object > Compound Path > Make | document, selection |  |  |
| menu_1199 | `noCompoundPath` | Object > Compound Path > Release | document, selection |  |  |
| menu_1200 | `setCropMarks` | Object > Artboards > Convert to Artboards | document, selection |  |  |
| menu_1201 | `ReArrange Artboards` | Object > Artboards > Rearrange All Artboards | document |  |  |
| menu_1202 | `Fit Artboard to artwork bounds` | Object > Artboards > Fit to Artwork Bounds | document |  |  |
| menu_1203 | `Switch Orientation` | Object > Artboards > Switch Orientation | document | >= 30.0 |  |
| menu_1204 | `Fit Artboard to selected Art` | Object > Artboards > Fit to Selected Art | document, selection |  |  |
| menu_1205 | `setGraphStyle` | Object > Graph > Type... | document |  |  |
| menu_1206 | `editGraphData` | Object > Graph > Data... | document, selection |  |  |
| menu_1207 | `graphDesigns` | Object > Graph > Design... | document, selection |  |  |
| menu_1208 | `setBarDesign` | Object > Graph > Column... | document, selection |  |  |
| menu_1209 | `setIconDesign` | Object > Graph > Marker... | document, selection |  |  |

## Other

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_2000 | `closeAll` | Close All | document | >= 29.4 |  |
| menu_1719 | `Debug Panel` | Debug Panel |  |  |  |

## Other Misc

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_2052 | `switchSelTool` | Other Misc > Switch Units | document | >= 29.4 |  |
| menu_2053 | `new2` | Other Misc > New File (No Dialog) |  | >= 29.4 |  |
| menu_2054 | `helpcontent2` | Other Misc > Help (Secondary) |  | >= 29.4 | ignored |
| menu_2055 | `undo2` | Other Misc > Undo (Secondary) | document | >= 29.4 | ignored |
| menu_2056 | `cut2` | Other Misc > Cut (Secondary) | document, selection | >= 29.4 | ignored |
| menu_2057 | `copy2` | Other Misc > Copy (Secondary) | document, selection | >= 29.4 | ignored |
| menu_2058 | `paste2` | Other Misc > Paste (Secondary) | document | >= 29.4 | ignored |
| menu_2059 | `zoomin2` | Other Misc > Zoom In (Secondary) | document | >= 29.4 | ignored |
| menu_2060 | `navigateToNextDocument` | Other Misc > Navigate to Next Document | document | >= 29.4 |  |
| menu_2061 | `navigateToPreviousDocument` | Other Misc > Navigate to Previous Document | document | >= 29.4 |  |
| menu_2062 | `navigateToNextDocumentGroup` | Other Misc > Navigate to Next Document Group | document | >= 29.4 |  |
| menu_2063 | `navigateToPreviousDocumentGroup` | Other Misc > Navigate to Previous Document Group | document | >= 29.4 |  |
| menu_2064 | `~subscript2` | Other Misc > Subscript (Secondary) | document, selection | >= 29.4 | ignored |
| menu_2065 | `~superScript2` | Other Misc > Superscript (Secondary) | document, selection | >= 29.4 | ignored |

## Other Object

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_2046 | `lock2` | Other Object > Lock Others | document, selection | >= 29.4 |  |
| menu_2047 | `hide2` | Other Object > Hide Others | document, selection | >= 29.4 |  |
| menu_2048 | `repeatPathfinder` | Other Object > Repeat Pathfinder | document, selection | >= 29.4 |  |
| menu_2049 | `avgAndJoin` | Other Object > Average & Join | document, selection | >= 29.4 |  |
| menu_2050 | `enterFocus` | Other Object > Isolate Selected Object | document, selection | >= 29.4 |  |
| menu_2051 | `exitFocus` | Other Object > Exit Isolation Mode | document, selection | >= 29.4 |  |

## Other Text

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_2020 | `faceSizeUp` | Other Text > Point Size Up | document, selection | >= 29.4 |  |
| menu_2021 | `faceSizeDown` | Other Text > Point Size Down | document, selection | >= 29.4 |  |
| menu_2022 | `sizeStepUp` | Other Text > Font Size Step Up | document, selection | >= 29.4 |  |
| menu_2023 | `sizeStepDown` | Other Text > Font Size Step Down | document, selection | >= 29.4 |  |
| menu_2024 | `~kernFurther` | Other Text > Kern Looser | document | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2025 | `~kernCloser` | Other Text > Kern Tighter | document | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2026 | `tracking` | Other Text > Tracking | document, selection | >= 29.4 |  |
| menu_2027 | `clearTrack` | Other Text > Clear Tracking | document, selection | >= 29.4 |  |
| menu_2028 | `spacing` | Other Text > Spacing | document, selection | >= 29.4 |  |
| menu_2029 | `clearTypeScale` | Other Text > Uniform Type | document, selection | >= 29.4 |  |
| menu_2030 | `highlightFont` | Other Text > Highlight Font | document, selection | >= 29.4 |  |
| menu_2031 | `highlightFont2` | Other Text > Highlight Font (Secondary) | document, selection | >= 29.4 |  |
| menu_2032 | `leftAlign` | Other Text > Left Align Text | document, selection | >= 29.4 |  |
| menu_2033 | `centerAlign` | Other Text > Center Text | document, selection | >= 29.4 |  |
| menu_2034 | `rightAlign` | Other Text > Right Align Text | document, selection | >= 29.4 |  |
| menu_2035 | `justify` | Other Text > Justify Text Left | document, selection | >= 29.4 |  |
| menu_2036 | `justifyCenter` | Other Text > Justify Text Center | document, selection | >= 29.4 |  |
| menu_2037 | `justifyRight` | Other Text > Justify Text Right | document, selection | >= 29.4 |  |
| menu_2038 | `justifyAll` | Other Text > Justify All Lines | document, selection | >= 29.4 |  |
| menu_2039 | `toggleAutoHyphen` | Other Text > Toggle Auto Hyphenation | document, selection | >= 29.4 |  |
| menu_2040 | `toggleLineComposer` | Other Text > Toggle Line Composer | document, selection | >= 29.4 |  |
| menu_2041 | `~subscript` | Other Text > Subscript | document, selection | >= 29.4 |  |
| menu_2042 | `~superScript` | Other Text > Superscript | document, selection | >= 29.4 |  |
| menu_2043 | `~textBold` | Other Text > Bold | document, selection | >= 29.4 |  |
| menu_2044 | `~textItalic` | Other Text > Italic | document, selection | >= 29.4 |  |
| menu_2045 | `~textUnderline` | Other Text > Underline | document, selection | >= 29.4 |  |

## Palette

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1694 | `Adobe Actions Batch` | Palette > Actions > Batch... |  |  |  |
| menu_1695 | `Adobe New Fill Shortcut` | Palette > Appearance > Add New Fill |  |  |  |
| menu_1696 | `Adobe New Stroke Shortcut` | Palette > Appearance > Add New Stroke |  |  |  |
| menu_1697 | `Adobe New Style Shortcut` | Palette > Graphic Styles > New Graphic Style... |  |  |  |
| menu_1698 | `AdobeLayerPalette2` | Palette > Layers > New Layer |  |  |  |
| menu_1699 | `AdobeLayerPalette3` | Palette > Layers > New Layer with Dialog... |  |  |  |
| menu_1700 | `Adobe Update Link Shortcut` | Palette > Links > Update Link |  |  |  |
| menu_1701 | `Adobe New Swatch Shortcut Menu` | Palette > Swatches > New Swatch... |  |  |  |
| menu_1702 | `Adobe New Symbol Shortcut` | Palette > Symbols > New Symbol... |  |  |  |

## Preferences

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1704 | `preference` | Preferences > General... |  |  |  |
| menu_1705 | `selectPref` | Preferences > Selection & Anchor Display... |  |  |  |
| menu_1706 | `keyboardPref` | Preferences > Type... |  |  |  |
| menu_1707 | `unitundoPref` | Preferences > Units... |  |  |  |
| menu_1708 | `guidegridPref` | Preferences > Guides & Grid... |  |  |  |
| menu_1709 | `snapPref` | Preferences > Smart Guides... |  |  |  |
| menu_1710 | `slicePref` | Preferences > Slices... |  |  |  |
| menu_1711 | `hyphenPref` | Preferences > Hyphenation... |  |  |  |
| menu_1712 | `pluginPref` | Preferences > Plug-ins & Scratch Disks... |  |  |  |
| menu_1713 | `UIPref` | Preferences > User Interface... |  |  |  |
| menu_1714 | `GPUPerformancePref` | Preferences > Performance |  | >= 19 |  |
| menu_1715 | `FilePref` | Preferences > File Handling... |  |  |  |
| menu_1716 | `ClipboardPref` | Preferences > Clipboard Handling |  | >= 25 |  |
| menu_1717 | `BlackPref` | Preferences > Appearance of Black... |  |  |  |
| menu_1718 | `DevicesPref` | Preferences > Devices |  | >= 24 |  |

## Select

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1238 | `selectall` | Select > All | document |  |  |
| menu_1239 | `selectallinartboard` | Select > All on Active Artboard | document |  |  |
| menu_1240 | `deselectall` | Select > Deselect | document, selection |  |  |
| menu_1241 | `Find Reselect menu item` | Select > Reselect | document, selection |  |  |
| menu_1242 | `Inverse menu item` | Select > Inverse | document |  |  |
| menu_1243 | `Selection Hat 8` | Select > Next Object Above | document, selection |  |  |
| menu_1244 | `Selection Hat 9` | Select > Next Object Below | document, selection |  |  |
| menu_1245 | `Find Appearance menu item` | Select > Same > Appearance | document |  |  |
| menu_1246 | `Find Appearance Attributes menu item` | Select > Same > Appearance Attribute | document, selection |  |  |
| menu_1247 | `Find Blending Mode menu item` | Select > Same > Blending Mode | document |  |  |
| menu_1248 | `Find Fill & Stroke menu item` | Select > Same > Fill & Stroke | document |  |  |
| menu_1249 | `Find Fill Color menu item` | Select > Same > Fill Color | document |  |  |
| menu_1250 | `Find Opacity menu item` | Select > Same > Opacity | document |  |  |
| menu_1251 | `Find Stroke Color menu item` | Select > Same > Stroke Color | document |  |  |
| menu_1252 | `Find Stroke Weight menu item` | Select > Same > Stroke Weight | document |  |  |
| menu_1253 | `Find Style menu item` | Select > Same > Graphic Style | document, selection |  |  |
| menu_1254 | `Find Live Shape menu item` | Select > Same > Shape | document, selection |  |  |
| menu_1255 | `Find Symbol Instance menu item` | Select > Same > Symbol Instance | document, selection |  |  |
| menu_1256 | `Find Link Block Series menu item` | Select > Same > Link Block Series | document, selection |  |  |
| menu_1257 | `Find Text Font Family menu item` | Select > Same > Font Family | document | >= 26 |  |
| menu_1258 | `Find Text Font Family Style menu item` | Select > Same > Font Family & Style | document | >= 26 |  |
| menu_1259 | `Find Text Font Family Style Size menu item` | Select > Same > Font Family, Style & Size | document | >= 26 |  |
| menu_1260 | `Find Text Font Size menu item` | Select > Same > Font Size | document | >= 26 |  |
| menu_1261 | `Find Text Fill Color menu item` | Select > Same > Text Fill Color | document | >= 26 |  |
| menu_1262 | `Find Text Stroke Color menu item` | Select > Same > Text Stroke Color | document | >= 26 |  |
| menu_1263 | `Find Text Fill Stroke Color menu item` | Select > Same > Text Fill & Stroke Color | document | >= 26 |  |
| menu_1264 | `Selection Hat 3` | Select > Object > All on Same Layers | document, selection |  |  |
| menu_1265 | `Selection Hat 1` | Select > Object > Direction Handles | document, selection |  |  |
| menu_1266 | `Bristle Brush Strokes menu item` | Select > Object > Bristle Brush Strokes | document |  |  |
| menu_1267 | `Brush Strokes menu item` | Select > Object > Brush Strokes | document |  |  |
| menu_1268 | `Clipping Masks menu item` | Select > Object > Clipping Masks | document |  |  |
| menu_1269 | `Stray Points menu item` | Select > Object > Stray Points | document |  |  |
| menu_1270 | `Text Objects menu item` | Select > Object > All Text Objects | document |  |  |
| menu_1271 | `Point Text Objects menu item` | Select > Object > Point Text Objects | document |  |  |
| menu_1272 | `Area Text Objects menu item` | Select > Object > Area Text Objects | document |  |  |
| menu_1273 | `SmartEdit Menu Item` | Select > Start/Stop Global Edit | document, selection | >= 23 |  |
| menu_1274 | `Selection Hat 10` | Select > Save Selection... | document, selection |  |  |
| menu_1275 | `Selection Hat 11` | Select > Edit Selection... | document, selection |  |  |
| menu_1276 | `Selection Hat 14` | Select > Update Selection | document, selection | >= 28 |  |

## Type

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1210 | `Browse Typekit Fonts Menu IllustratorUI` | Type > More from Adobe Fonts... |  | >= 17.1 |  |
| menu_1211 | `alternate glyph palette plugin` | Type > Glyphs |  |  |  |
| menu_1212 | `point-area` | Type > Convert to Area Type / Point Type | document, selection | >= 29.4 |  |
| menu_1213 | `area-type-options` | Type > Area Type Options... | document, selection |  |  |
| menu_1214 | `Rainbow` | Type > Type on a Path > Rainbow | document, selection |  |  |
| menu_1215 | `Skew` | Type > Type on a Path > Skew | document, selection |  |  |
| menu_1216 | `3D ribbon` | Type > Type on a Path > 3D Ribbon | document, selection |  |  |
| menu_1217 | `Stair Step` | Type > Type on a Path > Stair Step | document, selection |  |  |
| menu_1218 | `Gravity` | Type > Type on a Path > Gravity | document, selection |  |  |
| menu_1219 | `typeOnPathOptions` | Type > Type on a Path > Type on a Path Options... | document, selection |  |  |
| menu_1220 | `updateLegacyTOP` | Type > Type on a Path > Update Legacy Type on a Path | document, selection |  |  |
| menu_1221 | `threadTextCreate` | Type > Threaded Text > Create | document, selection |  |  |
| menu_1222 | `releaseThreadedTextSelection` | Type > Threaded Text > Release Selection | document, selection |  |  |
| menu_1223 | `removeThreading` | Type > Threaded Text > Remove Threading | document, selection |  |  |
| menu_1224 | `fitHeadline` | Type > Fit Headline | document, selection |  |  |
| menu_1225 | `Adobe IllustratorUI Resolve Missing Font` | Type > Resolve Missing Fonts... | document |  |  |
| menu_1226 | `Adobe Illustrator Find Font Menu Item` | Type > Find/Replace Font... | document |  |  |
| menu_1227 | `UpperCase Change Case Item` | Type > Change Case > UPPERCASE | document, selection |  |  |
| menu_1228 | `LowerCase Change Case Item` | Type > Change Case > lowercase | document, selection |  |  |
| menu_1229 | `Title Case Change Case Item` | Type > Change Case > Title Case | document, selection |  |  |
| menu_1230 | `Sentence case Change Case Item` | Type > Change Case > Sentence case | document, selection |  |  |
| menu_1231 | `Adobe Illustrator Smart Punctuation Menu Item` | Type > Smart Punctuation... | document |  |  |
| menu_1232 | `outline` | Type > Create Outlines | document, selection |  |  |
| menu_1233 | `Adobe Optical Alignment Item` | Type > Optical Margin Alignment | document, selection |  |  |
| menu_1234 | `convert list style to text` | Type > Bullets and Numbering > Convert to text | document, selection | >= 27.1 |  |
| menu_2001 | `~bullet` | Type > Insert Special Character > Symbols > Bullet | document | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2002 | `~copyright` | Type > Insert Special Character > Symbols > Copyright Symbol | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2003 | `~ellipsis` | Type > Insert Special Character > Symbols > Ellipsis | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2004 | `~paragraphSymbol` | Type > Insert Special Character > Symbols > Paragraph Symbol | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2005 | `~registeredTrademark` | Type > Insert Special Character > Symbols > Registered Trademark Symbol | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2006 | `~sectionSymbol` | Type > Insert Special Character > Symbols > Section Symbol | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2007 | `~trademarkSymbol` | Type > Insert Special Character > Symbols > Trademark Symbol | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2008 | `~emDash` | Type > Insert Special Character > Hyphens And Dashes > Em Dash | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2009 | `~enDash` | Type > Insert Special Character > Hyphens And Dashes > En Dash | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2010 | `~discretionaryHyphen` | Type > Insert Special Character > Hyphens And Dashes > Discretionary Hyphen | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2011 | `~doubleLeftQuote` | Type > Insert Special Character > Quotation Marks > Double Left Quotation Marks | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2012 | `~doubleRightQuote` | Type > Insert Special Character > Quotation Marks > Double Right Quotation Marks | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2013 | `~singleLeftQuote` | Type > Insert Special Character > Quotation Marks > Single Left Quotation Marks | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2014 | `~singleRightQuote` | Type > Insert Special Character > Quotation Marks > Single Right Quotation Marks | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2015 | `~emSpace` | Type > Insert WhiteSpace Character > Em Space | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2016 | `~enSpace` | Type > Insert WhiteSpace Character > En Space | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2017 | `~hairSpace` | Type > Insert WhiteSpace Character > Hair Space | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2018 | `~thinSpace` | Type > Insert WhiteSpace Character > Thin Space | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_2019 | `~forcedLineBreak` | Type > Insert Break Character > Forced Line Break | document, selection | >= 29.4 | A selection is technically required but Illustrator does not recognize an active text selection when the text cursor is placed inside text (which is what these commands expect) |
| menu_1235 | `showHiddenChar` | Type > Show Hidden Characters | document |  |  |
| menu_1236 | `type-horizontal` | Type > Type Orientation > Horizontal | document, selection |  |  |
| menu_1237 | `type-vertical` | Type > Type Orientation > Vertical | document, selection |  |  |

## View

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1396 | `preview` | View > Outline / Preview | document |  |  |
| menu_1397 | `GPU Preview` | View > GPU Preview / Preview on CPU | document |  |  |
| menu_1398 | `ink` | View > Overprint Preview | document |  |  |
| menu_1399 | `raster` | View > Pixel Preview | document |  |  |
| menu_1400 | `proof-document` | View > Proof Setup > Working CMYK | document |  |  |
| menu_1401 | `proof-mac-rgb` | View > Proof Setup > Legacy Macintosh RGB (Gamma 1.8) | document |  |  |
| menu_1402 | `proof-win-rgb` | View > Proof Setup > Internet Standard RGB (sRGB) | document |  |  |
| menu_1403 | `proof-monitor-rgb` | View > Proof Setup > Monitor RGB | document |  |  |
| menu_1404 | `proof-colorblindp` | View > Proof Setup > Color blindness - Protanopia-type | document |  |  |
| menu_1405 | `proof-colorblindd` | View > Proof Setup > Color blindness - Deuteranopia-type | document |  |  |
| menu_1406 | `proof-custom` | View > Proof Setup > Customize... | document |  |  |
| menu_1407 | `proofColors` | View > Proof Colors | document |  |  |
| menu_1408 | `zoomin` | View > Zoom In | document |  |  |
| menu_1409 | `zoomout` | View > Zoom Out | document |  |  |
| menu_1410 | `fitin` | View > Fit Artboard in Window | document |  |  |
| menu_1411 | `fitall` | View > Fit All in Window | document |  |  |
| menu_1412 | `AISlice Feedback Menu` | View > Show / Hide Slices |  |  |  |
| menu_1413 | `AISlice Lock Menu` | View > Lock Slices |  |  |  |
| menu_1414 | `AI Bounding Box Toggle` | View > Show / Hide Bounding Box |  |  |  |
| menu_1415 | `TransparencyGrid Menu Item` | View > Show / Hide Transparency Grid | document |  |  |
| menu_1416 | `actualsize` | View > Actual Size | document |  |  |
| menu_1417 | `Show Gaps Planet X` | View > Show / Hide Live Paint Gaps |  |  |  |
| menu_1418 | `Gradient Feedback` | View > Show / Hide Gradient Annotator |  |  |  |
| menu_1419 | `Live Corner Annotator` | View > Show / Hide Corner Widget |  | >= 17.1 |  |
| menu_1420 | `edge` | View > Show / Hide Edges | document |  |  |
| menu_1421 | `Snapomatic on-off menu item` | View > Smart Guides |  |  |  |
| menu_1422 | `Show Perspective Grid` | View > Perspective Grid > Show / Hide Grid | document |  |  |
| menu_1423 | `Show Ruler` | View > Perspective Grid > Show / Hide Rulers | document |  |  |
| menu_1424 | `Snap to Grid` | View > Perspective Grid > Snap to Grid | document |  |  |
| menu_1425 | `Lock Perspective Grid` | View > Perspective Grid > Lock Grid | document |  |  |
| menu_1426 | `Lock Station Point` | View > Perspective Grid > Lock Station Point | document |  |  |
| menu_1427 | `Define Perspective Grid` | View > Perspective Grid > Define Grid | document |  |  |
| menu_1428 | `Save Perspective Grid as Preset` | View > Perspective Grid > Save Grid as Preset | document |  |  |
| menu_1429 | `artboard` | View > Show / Hide Artboards | document |  |  |
| menu_1430 | `pagetiling` | View > Show / Hide Print Tiling | document |  |  |
| menu_1431 | `showtemplate` | View > Show / Hide Template | document |  |  |
| menu_1432 | `ruler` | View > Rulers > Show / Hide Rulers | document |  |  |
| menu_1433 | `rulerCoordinateSystem` | View > Rulers > Change to Global Rulers | document |  |  |
| menu_1434 | `videoruler` | View > Rulers > Show / Hide Video Rulers | document |  |  |
| menu_1435 | `textthreads` | View > Show / Hide Text Threads | document |  |  |
| menu_1436 | `showguide` | View > Guides > Show / Hide Guides | document |  |  |
| menu_1437 | `lockguide` | View > Guides > Lock / Unlock Guides | document |  |  |
| menu_1438 | `makeguide` | View > Guides > Make Guides | document, selection |  |  |
| menu_1439 | `releaseguide` | View > Guides > Release Guides | document |  |  |
| menu_1440 | `clearguide` | View > Guides > Clear Guides | document |  |  |
| menu_1441 | `showgrid` | View > Show / Hide Grid | document |  |  |
| menu_1442 | `snapgrid` | View > Snap to Grid | document |  |  |
| menu_1443 | `snappoint` | View > Snap to Point | document |  |  |
| menu_1444 | `newview` | View > New View... | document |  |  |
| menu_1445 | `editview` | View > Edit Views... | document |  |  |

## Window

| ID | Command value | Menu path | Requires | Version | Notes |
|---|---|---|---|---|---|
| menu_1446 | `newwindow` | Window > New Window | document |  |  |
| menu_1447 | `cascade` | Window > Arrange > Cascade | document |  |  |
| menu_1448 | `tile` | Window > Arrange > Tile | document |  |  |
| menu_1449 | `floatInWindow` | Window > Arrange > Float in Window | document |  |  |
| menu_1450 | `floatAllInWindows` | Window > Arrange > Float All in Windows | document |  |  |
| menu_1451 | `consolidateAllWindows` | Window > Arrange > Consolidate All Windows | document |  |  |
| menu_1452 | `Browse Add-Ons Menu` | Window > Find Extensions on Exchange... |  | >= 19 |  |
| menu_1453 | `Adobe Reset Workspace` | Window > Reset Workspace |  |  |  |
| menu_1454 | `Adobe New Workspace` | Window > Workspace > New Workspace... |  |  |  |
| menu_1455 | `Adobe Manage Workspace` | Window > Workspace > Manage Workspaces... |  |  |  |
| menu_1456 | `_GenericPluginMenuItem 25` | Window > Contextual Task Bar |  | >= 27.9 | ignored |
| menu_1457 | `drover control palette plugin` | Window > Control |  |  |  |
| menu_1458 | `Adobe Advanced Toolbar Menu` | Window > Toolbars > Advanced |  | >= 23 |  |
| menu_1459 | `Adobe Basic Toolbar Menu` | Window > Toolbars > Basic |  | >= 23 |  |
| menu_1460 | `Adobe Quick Toolbar Menu` | Window > Toolbars > Getting Started |  | >= 29.3 |  |
| menu_1461 | `New Tools Panel` | Window > Toolbars > New Toolbar... |  | >= 17 |  |
| menu_1462 | `Manage Tools Panel` | Window > Toolbars > Manage Toolbar... |  | >= 17 |  |
| menu_1463 | `Adobe 3D Panel` | Window > 3D and Materials |  | >= 26 |  |
| menu_1464 | `Adobe Action Palette` | Window > Actions |  |  |  |
| menu_1465 | `AdobeAlignObjects2` | Window > Align |  |  |  |
| menu_1466 | `Style Palette` | Window > Appearance |  |  |  |
| menu_1467 | `Adobe Artboard Palette` | Window > Artboards |  |  |  |
| menu_1468 | `Adobe SmartExport Panel Menu Item` | Window > Asset Export |  | >= 20 |  |
| menu_1469 | `internal palettes posing as plug-in menus-attributes` | Window > Attributes |  |  |  |
| menu_1470 | `Adobe BrushManager Menu Item` | Window > Brushes |  |  |  |
| menu_1471 | `Adobe Color Palette` | Window > Color |  |  |  |
| menu_1472 | `Adobe Harmony Palette` | Window > Color Guide |  |  |  |
| menu_1473 | `Adobe Illustrator Kuler Panel` | Window > Color Themes |  | 22-25.9 |  |
| menu_1474 | `Adobe Commenting Palette` | Window > Comments |  | >= 26 |  |
| menu_1475 | `CSS Menu Item` | Window > CSS Properties |  |  |  |
| menu_1476 | `DocInfo1` | Window > Document Info |  |  |  |
| menu_1477 | `Adobe Flattening Preview` | Window > Flattener Preview |  |  |  |
| menu_1478 | `Adobe Generative Patterns Panel` | Window > Generate Patterns | document | 28.6-29.999 |  |
| menu_1479 | `Generate` | Window > Generated Variations |  | >= 28 |  |
| menu_1480 | `Adobe Gradient Palette` | Window > Gradient |  |  |  |
| menu_1481 | `Adobe Style Palette` | Window > Graphic Styles |  |  |  |
| menu_1482 | `Adobe HistoryPanel Menu Item` | Window > History |  | 26.4-26.9 |  |
| menu_1483 | `Adobe History Panel Menu Item` | Window > History |  | >= 27 |  |
| menu_1484 | `Adobe Vectorize Panel` | Window > Image Trace |  |  |  |
| menu_1485 | `internal palettes posing as plug-in menus-info` | Window > Info |  |  |  |
| menu_1486 | `AdobeLayerPalette1` | Window > Layers |  |  |  |
| menu_1487 | `Adobe Learn Panel Menu Item` | Window > Learn |  | 22-25.9 |  |
| menu_1488 | `Adobe CSXS Extension com.adobe.DesignLibraries.angularLibraries` | Window > Libraries |  |  |  |
| menu_1489 | `Adobe LinkPalette Menu Item` | Window > Links |  |  |  |
| menu_1490 | `AI Magic Wand` | Window > Magic Wand |  |  |  |
| menu_1491 | `Adobe Vector Edge Panel` | Window > Mockup |  | >= 28 |  |
| menu_1492 | `AdobeNavigator` | Window > Navigator |  |  |  |
| menu_1493 | `Adobe PathfinderUI` | Window > Pathfinder |  |  |  |
| menu_1494 | `Adobe Pattern Panel Toggle` | Window > Pattern Options |  |  |  |
| menu_1495 | `Adobe Property Palette` | Window > Properties |  | >= 26 | ignored |
| menu_1496 | `ReTypeWindowMenu` | Window > Retype |  | >= 27.6 |  |
| menu_1497 | `Adobe Separation Preview Panel` | Window > Separations Preview |  |  |  |
| menu_1498 | `Adobe Stroke Palette` | Window > Stroke |  |  |  |
| menu_1499 | `Adobe SVG Interactivity Palette` | Window > SVG Interactivity |  |  |  |
| menu_1500 | `Adobe Swatches Menu Item` | Window > Swatches |  |  |  |
| menu_1501 | `Adobe Symbol Palette` | Window > Symbols |  |  |  |
| menu_1502 | `AdobeTransformObjects1` | Window > Transform |  |  |  |
| menu_1503 | `Adobe Transparency Palette Menu Item` | Window > Transparency |  |  |  |
| menu_1504 | `internal palettes posing as plug-in menus-character` | Window > Type > Character |  |  |  |
| menu_1505 | `Character Styles` | Window > Type > Character Styles |  |  |  |
| menu_1506 | `alternate glyph palette plugin 2` | Window > Type > Glyphs |  |  |  |
| menu_1507 | `internal palettes posing as plug-in menus-opentype` | Window > Type > OpenType |  |  |  |
| menu_1508 | `internal palettes posing as plug-in menus-paragraph` | Window > Type > Paragraph |  |  |  |
| menu_1509 | `Adobe Paragraph Styles Palette` | Window > Type > Paragraph Styles |  |  |  |
| menu_1510 | `ReflowWindowMenu` | Window > Type > Reflow Viewer |  | >= 29 | East asian feature |
| menu_1511 | `internal palettes posing as plug-in menus-tab` | Window > Type > Tabs |  |  |  |
| menu_1512 | `Adobe Variables Palette Menu Item` | Window > Variables |  |  |  |
| menu_1513 | `Adobe Version History File Menu Item` | Window > Version History |  | >= 26 |  |
| menu_1514 | `_Brush Library Menu Item 1` | Window > Brush Libraries > Arrows > Arrows_Special |  |  | ignored |
| menu_1515 | `_Brush Library Menu Item 2` | Window > Brush Libraries > Arrows > Arrows_Standard |  |  | ignored |
| menu_1516 | `_Brush Library Menu Item 3` | Window > Brush Libraries > Arrows > Pattern Arrows |  |  | ignored |
| menu_1517 | `_Brush Library Menu Item 5` | Window > Brush Libraries > Artistic > Artistic_Calligraphic |  |  | ignored |
| menu_1518 | `_Brush Library Menu Item 6` | Window > Brush Libraries > Artistic > Artistic_ChalkCharcoalPencil |  |  | ignored |
| menu_1519 | `_Brush Library Menu Item 7` | Window > Brush Libraries > Artistic > Artistic_Ink |  |  | ignored |
| menu_1520 | `_Brush Library Menu Item 8` | Window > Brush Libraries > Artistic > Artistic_Paintbrush |  |  | ignored |
| menu_1521 | `_Brush Library Menu Item 9` | Window > Brush Libraries > Artistic > Artistic_ScrollPen |  |  | ignored |
| menu_1522 | `_Brush Library Menu Item 10` | Window > Brush Libraries > Artistic > Artistic_Watercolor |  |  | ignored |
| menu_1523 | `_Brush Library Menu Item 12` | Window > Brush Libraries > Borders > Borders_Dashed |  |  | ignored |
| menu_1524 | `_Brush Library Menu Item 13` | Window > Brush Libraries > Borders > Borders_Decorative |  |  | ignored |
| menu_1525 | `_Brush Library Menu Item 14` | Window > Brush Libraries > Borders > Borders_Frames |  |  | ignored |
| menu_1526 | `_Brush Library Menu Item 15` | Window > Brush Libraries > Borders > Borders_Geometric |  |  | ignored |
| menu_1527 | `_Brush Library Menu Item 16` | Window > Brush Libraries > Borders > Borders_Indigenous |  |  | ignored |
| menu_1528 | `_Brush Library Menu Item 17` | Window > Brush Libraries > Borders > Borders_Lines |  |  | ignored |
| menu_1529 | `_Brush Library Menu Item 18` | Window > Brush Libraries > Borders > Borders_Novelty |  |  | ignored |
| menu_1530 | `_Brush Library Menu Item 20` | Window > Brush Libraries > Bristle Brush > Bristle Brush Library |  |  | ignored |
| menu_1531 | `_Brush Library Menu Item 22` | Window > Brush Libraries > Decorative > Decorative_Banners and Seals |  |  | ignored |
| menu_1532 | `_Brush Library Menu Item 23` | Window > Brush Libraries > Decorative > Decorative_Scatter |  |  | ignored |
| menu_1533 | `_Brush Library Menu Item 24` | Window > Brush Libraries > Decorative > Decorative_Text Dividers |  |  | ignored |
| menu_1534 | `_Brush Library Menu Item 25` | Window > Brush Libraries > Decorative > Elegant Curl & Floral Brush Set |  |  | ignored |
| menu_1535 | `_Brush Library Menu Item 27` | Window > Brush Libraries > Image Brush > Image Brush Library |  |  | ignored |
| menu_1536 | `_Brush Library Menu Item 29` | Window > Brush Libraries > Vector Packs > Grunge brushes vector pack |  |  | ignored |
| menu_1537 | `_Brush Library Menu Item 30` | Window > Brush Libraries > Vector Packs > Hand Drawn brushes vector pack |  |  | ignored |
| menu_1538 | `_Brush Library Menu Item 32` | Window > Brush Libraries > Wacom 6D Brushes > 6d Art Pen Brushes |  |  | ignored |
| menu_1539 | `AdobeBrushMgrUI Other libraries menu item` | Window > Brush Libraries > Other Library |  |  |  |
| menu_1540 | `_Art Style Library Menu Item 0` | Window > Graphic Style Libraries > 3D Effects |  |  | ignored |
| menu_1541 | `_Art Style Library Menu Item 1` | Window > Graphic Style Libraries > Additive for Blob Brush |  |  | ignored |
| menu_1542 | `_Art Style Library Menu Item 2` | Window > Graphic Style Libraries > Additive |  |  | ignored |
| menu_1543 | `_Art Style Library Menu Item 3` | Window > Graphic Style Libraries > Artistic Effects |  |  | ignored |
| menu_1544 | `_Art Style Library Menu Item 4` | Window > Graphic Style Libraries > Buttons and Rollovers |  |  | ignored |
| menu_1545 | `_Art Style Library Menu Item 5` | Window > Graphic Style Libraries > Illuminate Styles |  |  | ignored |
| menu_1546 | `_Art Style Library Menu Item 6` | Window > Graphic Style Libraries > Image Effects |  |  | ignored |
| menu_1547 | `_Art Style Library Menu Item 7` | Window > Graphic Style Libraries > Neon Effects |  |  | ignored |
| menu_1548 | `_Art Style Library Menu Item 8` | Window > Graphic Style Libraries > Scribble Effects |  |  | ignored |
| menu_1549 | `_Art Style Library Menu Item 9` | Window > Graphic Style Libraries > Textures |  |  | ignored |
| menu_1550 | `_Art Style Library Menu Item 10` | Window > Graphic Style Libraries > Type Effects |  |  | ignored |
| menu_1551 | `_Art Style Library Menu Item 11` | Window > Graphic Style Libraries > Vonster Pattern Styles |  |  | ignored |
| menu_1552 | `Adobe Art Style Plugin Other libraries menu item` | Window > Graphic Style Libraries > Other Library... |  |  |  |
| menu_1553 | `_Swatch Library Menu Item 1` | Window > Swatch Libraries > Art History > Ancient |  |  | ignored |
| menu_1554 | `_Swatch Library Menu Item 2` | Window > Swatch Libraries > Art History > Baroque |  |  | ignored |
| menu_1555 | `_Swatch Library Menu Item 3` | Window > Swatch Libraries > Art History > Impressionism |  |  | ignored |
| menu_1556 | `_Swatch Library Menu Item 4` | Window > Swatch Libraries > Art History > Middle Ages |  |  | ignored |
| menu_1557 | `_Swatch Library Menu Item 5` | Window > Swatch Libraries > Art History > Pop Art |  |  | ignored |
| menu_1558 | `_Swatch Library Menu Item 6` | Window > Swatch Libraries > Art History > Prehistoric |  |  | ignored |
| menu_1559 | `_Swatch Library Menu Item 7` | Window > Swatch Libraries > Art History > Renaissance |  |  | ignored |
| menu_1560 | `_Swatch Library Menu Item 8` | Window > Swatch Libraries > Art History > Russian Poster Art |  |  | ignored |
| menu_1561 | `_Swatch Library Menu Item 9` | Window > Swatch Libraries > Celebration |  |  | ignored |
| menu_1562 | `_Swatch Library Menu Item 11` | Window > Swatch Libraries > Color Books > ANPA Color |  |  | ignored |
| menu_1563 | `_Swatch Library Menu Item 12` | Window > Swatch Libraries > Color Books > DIC Color Guide |  |  | ignored |
| menu_1564 | `_Swatch Library Menu Item 13` | Window > Swatch Libraries > Color Books > FOCOLTONE |  |  | ignored |
| menu_1565 | `_Swatch Library Menu Item 15` | Window > Swatch Libraries > Color Books > HKS E |  |  | ignored |
| menu_1566 | `_Swatch Library Menu Item 14` | Window > Swatch Libraries > Color Books > HKS E Process |  |  | ignored |
| menu_1567 | `_Swatch Library Menu Item 17` | Window > Swatch Libraries > Color Books > HKS K |  |  | ignored |
| menu_1568 | `_Swatch Library Menu Item 16` | Window > Swatch Libraries > Color Books > HKS K Process |  |  | ignored |
| menu_1569 | `_Swatch Library Menu Item 19` | Window > Swatch Libraries > Color Books > HKS N |  |  | ignored |
| menu_1570 | `_Swatch Library Menu Item 18` | Window > Swatch Libraries > Color Books > HKS N Process |  |  | ignored |
| menu_1571 | `_Swatch Library Menu Item 21` | Window > Swatch Libraries > Color Books > HKS Z |  |  | ignored |
| menu_1572 | `_Swatch Library Menu Item 20` | Window > Swatch Libraries > Color Books > HKS Z Process |  |  | ignored |
| menu_1573 | `_Swatch Library Menu Item 22` | Window > Swatch Libraries > Color Books > PANTONE+ CMYK Coated |  |  | ignored |
| menu_1574 | `_Swatch Library Menu Item 23` | Window > Swatch Libraries > Color Books > PANTONE+ CMYK Uncoated |  |  | ignored |
| menu_1575 | `_Swatch Library Menu Item 24` | Window > Swatch Libraries > Color Books > PANTONE+ Color Bridge Coated |  |  | ignored |
| menu_1576 | `_Swatch Library Menu Item 25` | Window > Swatch Libraries > Color Books > PANTONE+ Color Bridge Uncoated |  |  | ignored |
| menu_1577 | `_Swatch Library Menu Item 26` | Window > Swatch Libraries > Color Books > PANTONE+ Metallic Coated |  |  | ignored |
| menu_1578 | `_Swatch Library Menu Item 27` | Window > Swatch Libraries > Color Books > PANTONE+ Pastels & Neons Coated |  |  | ignored |
| menu_1579 | `_Swatch Library Menu Item 28` | Window > Swatch Libraries > Color Books > PANTONE+ Pastels & Neons Uncoated |  |  | ignored |
| menu_1580 | `_Swatch Library Menu Item 29` | Window > Swatch Libraries > Color Books > PANTONE+ Premium Metallics Coated |  |  | ignored |
| menu_1581 | `_Swatch Library Menu Item 30` | Window > Swatch Libraries > Color Books > PANTONE+ Solid Coated |  |  | ignored |
| menu_1582 | `_Swatch Library Menu Item 31` | Window > Swatch Libraries > Color Books > PANTONE+ Solid Uncoated |  |  | ignored |
| menu_1583 | `_Swatch Library Menu Item 32` | Window > Swatch Libraries > Color Books > TOYO 94 COLOR FINDER |  |  | ignored |
| menu_1584 | `_Swatch Library Menu Item 33` | Window > Swatch Libraries > Color Books > TOYO COLOR FINDER |  |  | ignored |
| menu_1585 | `_Swatch Library Menu Item 34` | Window > Swatch Libraries > Color Books > TRUMATCH |  |  | ignored |
| menu_1586 | `_Swatch Library Menu Item 36` | Window > Swatch Libraries > Color Properties > Bright |  |  | ignored |
| menu_1587 | `_Swatch Library Menu Item 37` | Window > Swatch Libraries > Color Properties > Cool |  |  | ignored |
| menu_1588 | `_Swatch Library Menu Item 38` | Window > Swatch Libraries > Color Properties > Dark |  |  | ignored |
| menu_1589 | `_Swatch Library Menu Item 39` | Window > Swatch Libraries > Color Properties > Desaturated |  |  | ignored |
| menu_1590 | `_Swatch Library Menu Item 40` | Window > Swatch Libraries > Color Properties > Light |  |  | ignored |
| menu_1591 | `_Swatch Library Menu Item 41` | Window > Swatch Libraries > Color Properties > Saturated |  |  | ignored |
| menu_1592 | `_Swatch Library Menu Item 42` | Window > Swatch Libraries > Color Properties > Soft |  |  | ignored |
| menu_1593 | `_Swatch Library Menu Item 43` | Window > Swatch Libraries > Color Properties > Warm |  |  | ignored |
| menu_1594 | `_Swatch Library Menu Item 44` | Window > Swatch Libraries > Corporate |  |  | ignored |
| menu_1595 | `_Swatch Library Menu Item 46` | Window > Swatch Libraries > Default Swatches > Art & Illustration |  |  | ignored |
| menu_1596 | `_Swatch Library Menu Item 47` | Window > Swatch Libraries > Default Swatches > Mobile |  |  | ignored |
| menu_1597 | `_Swatch Library Menu Item 48` | Window > Swatch Libraries > Default Swatches > Print |  |  | ignored |
| menu_1598 | `_Swatch Library Menu Item 49` | Window > Swatch Libraries > Default Swatches > Video and Film |  |  | ignored |
| menu_1599 | `_Swatch Library Menu Item 50` | Window > Swatch Libraries > Default Swatches > Web |  |  | ignored |
| menu_1600 | `_Swatch Library Menu Item 51` | Window > Swatch Libraries > Earthtone |  |  | ignored |
| menu_1601 | `_Swatch Library Menu Item 53` | Window > Swatch Libraries > Foods > Beverages |  |  | ignored |
| menu_1602 | `_Swatch Library Menu Item 54` | Window > Swatch Libraries > Foods > Fruit |  |  | ignored |
| menu_1603 | `_Swatch Library Menu Item 55` | Window > Swatch Libraries > Foods > Ice Cream |  |  | ignored |
| menu_1604 | `_Swatch Library Menu Item 56` | Window > Swatch Libraries > Foods > Sweets |  |  | ignored |
| menu_1605 | `_Swatch Library Menu Item 57` | Window > Swatch Libraries > Foods > Vegetables |  |  | ignored |
| menu_1606 | `_Swatch Library Menu Item 59` | Window > Swatch Libraries > Gradients > Brights |  |  | ignored |
| menu_1607 | `_Swatch Library Menu Item 60` | Window > Swatch Libraries > Gradients > Color Combinations |  |  | ignored |
| menu_1608 | `_Swatch Library Menu Item 61` | Window > Swatch Libraries > Gradients > Color Harmonies |  |  | ignored |
| menu_1609 | `_Swatch Library Menu Item 62` | Window > Swatch Libraries > Gradients > Earthtones |  |  | ignored |
| menu_1610 | `_Swatch Library Menu Item 63` | Window > Swatch Libraries > Gradients > Fades |  |  | ignored |
| menu_1611 | `_Swatch Library Menu Item 64` | Window > Swatch Libraries > Gradients > Foliage |  |  | ignored |
| menu_1612 | `_Swatch Library Menu Item 65` | Window > Swatch Libraries > Gradients > Fruits and Vegetables |  |  | ignored |
| menu_1613 | `_Swatch Library Menu Item 66` | Window > Swatch Libraries > Gradients > Gems and Jewels |  |  | ignored |
| menu_1614 | `_Swatch Library Menu Item 67` | Window > Swatch Libraries > Gradients > Metals |  |  | ignored |
| menu_1615 | `_Swatch Library Menu Item 68` | Window > Swatch Libraries > Gradients > Neutrals |  |  | ignored |
| menu_1616 | `_Swatch Library Menu Item 69` | Window > Swatch Libraries > Gradients > Pastels |  |  | ignored |
| menu_1617 | `_Swatch Library Menu Item 70` | Window > Swatch Libraries > Gradients > Seasons |  |  | ignored |
| menu_1618 | `_Swatch Library Menu Item 71` | Window > Swatch Libraries > Gradients > Simple Radial |  |  | ignored |
| menu_1619 | `_Swatch Library Menu Item 72` | Window > Swatch Libraries > Gradients > Skintones |  |  | ignored |
| menu_1620 | `_Swatch Library Menu Item 73` | Window > Swatch Libraries > Gradients > Sky |  |  | ignored |
| menu_1621 | `_Swatch Library Menu Item 74` | Window > Swatch Libraries > Gradients > Spectrums |  |  | ignored |
| menu_1622 | `_Swatch Library Menu Item 75` | Window > Swatch Libraries > Gradients > Stone and Brick |  |  | ignored |
| menu_1623 | `_Swatch Library Menu Item 76` | Window > Swatch Libraries > Gradients > Tints and Shades |  |  | ignored |
| menu_1624 | `_Swatch Library Menu Item 77` | Window > Swatch Libraries > Gradients > Vignettes |  |  | ignored |
| menu_1625 | `_Swatch Library Menu Item 78` | Window > Swatch Libraries > Gradients > Water |  |  | ignored |
| menu_1626 | `_Swatch Library Menu Item 79` | Window > Swatch Libraries > Gradients > Wood |  |  | ignored |
| menu_1627 | `_Swatch Library Menu Item 80` | Window > Swatch Libraries > Kids Stuff |  |  | ignored |
| menu_1628 | `_Swatch Library Menu Item 81` | Window > Swatch Libraries > Metal |  |  | ignored |
| menu_1629 | `_Swatch Library Menu Item 83` | Window > Swatch Libraries > Nature > Beach |  |  | ignored |
| menu_1630 | `_Swatch Library Menu Item 84` | Window > Swatch Libraries > Nature > Flowers |  |  | ignored |
| menu_1631 | `_Swatch Library Menu Item 85` | Window > Swatch Libraries > Nature > Foliage |  |  | ignored |
| menu_1632 | `_Swatch Library Menu Item 86` | Window > Swatch Libraries > Nature > Landscape |  |  | ignored |
| menu_1633 | `_Swatch Library Menu Item 87` | Window > Swatch Libraries > Nature > Seasons |  |  | ignored |
| menu_1634 | `_Swatch Library Menu Item 88` | Window > Swatch Libraries > Nature > Stone and Brick |  |  | ignored |
| menu_1635 | `_Swatch Library Menu Item 89` | Window > Swatch Libraries > Neutral |  |  | ignored |
| menu_1636 | `_Swatch Library Menu Item 92` | Window > Swatch Libraries > Patterns > Basic Graphics > Basic Graphics_Dots |  |  | ignored |
| menu_1637 | `_Swatch Library Menu Item 93` | Window > Swatch Libraries > Patterns > Basic Graphics > Basic Graphics_Lines |  |  | ignored |
| menu_1638 | `_Swatch Library Menu Item 94` | Window > Swatch Libraries > Patterns > Basic Graphics > Basic Graphics_Textures |  |  | ignored |
| menu_1639 | `_Swatch Library Menu Item 96` | Window > Swatch Libraries > Patterns > Decorative > Decorative Legacy |  |  | ignored |
| menu_1640 | `_Swatch Library Menu Item 97` | Window > Swatch Libraries > Patterns > Decorative > Vonster Patterns |  |  | ignored |
| menu_1641 | `_Swatch Library Menu Item 99` | Window > Swatch Libraries > Patterns > Nature > Nature_Animal Skins |  |  | ignored |
| menu_1642 | `_Swatch Library Menu Item 100` | Window > Swatch Libraries > Patterns > Nature > Nature_Foliage |  |  | ignored |
| menu_1643 | `_Swatch Library Menu Item 102` | Window > Swatch Libraries > Scientific > Analogous |  |  | ignored |
| menu_1644 | `_Swatch Library Menu Item 103` | Window > Swatch Libraries > Scientific > Complementary |  |  | ignored |
| menu_1645 | `_Swatch Library Menu Item 104` | Window > Swatch Libraries > Scientific > Split Complementary |  |  | ignored |
| menu_1646 | `_Swatch Library Menu Item 105` | Window > Swatch Libraries > Scientific > Tetrad |  |  | ignored |
| menu_1647 | `_Swatch Library Menu Item 106` | Window > Swatch Libraries > Scientific > Triad |  |  | ignored |
| menu_1648 | `_Swatch Library Menu Item 107` | Window > Swatch Libraries > Skintones |  |  | ignored |
| menu_1649 | `_Swatch Library Menu Item 108` | Window > Swatch Libraries > System (Macintosh) |  |  | ignored |
| menu_1650 | `_Swatch Library Menu Item 109` | Window > Swatch Libraries > System (Windows) |  |  | ignored |
| menu_1651 | `_Swatch Library Menu Item 110` | Window > Swatch Libraries > Textiles |  |  | ignored |
| menu_1652 | `_Swatch Library Menu Item 111` | Window > Swatch Libraries > VisiBone2 |  |  | ignored |
| menu_1653 | `_Swatch Library Menu Item 112` | Window > Swatch Libraries > Web |  |  | ignored |
| menu_1654 | `AdobeSwatch_ Other libraries menu item` | Window > Swatch Libraries > Other Library... |  |  |  |
| menu_1655 | `_Base Library Menu Item 0` | Window > Symbol Libraries > 3D Symbols |  |  | ignored |
| menu_1656 | `_Base Library Menu Item 1` | Window > Symbol Libraries > Arrows |  |  | ignored |
| menu_1657 | `_Base Library Menu Item 2` | Window > Symbol Libraries > Artistic Textures |  |  | ignored |
| menu_1658 | `_Base Library Menu Item 3` | Window > Symbol Libraries > Celebration |  |  | ignored |
| menu_1659 | `_Base Library Menu Item 4` | Window > Symbol Libraries > Charts |  |  | ignored |
| menu_1660 | `_Base Library Menu Item 5` | Window > Symbol Libraries > Communication |  |  | ignored |
| menu_1661 | `_Base Library Menu Item 6` | Window > Symbol Libraries > Dot Pattern Vector Pack |  |  | ignored |
| menu_1662 | `_Base Library Menu Item 7` | Window > Symbol Libraries > Fashion |  |  | ignored |
| menu_1663 | `_Base Library Menu Item 8` | Window > Symbol Libraries > Florid Vector Pack |  |  | ignored |
| menu_1664 | `_Base Library Menu Item 9` | Window > Symbol Libraries > Flowers |  |  | ignored |
| menu_1665 | `_Base Library Menu Item 10` | Window > Symbol Libraries > Grime Vector Pack |  |  | ignored |
| menu_1666 | `_Base Library Menu Item 11` | Window > Symbol Libraries > Hair and Fur |  |  | ignored |
| menu_1667 | `_Base Library Menu Item 12` | Window > Symbol Libraries > Heirloom |  |  | ignored |
| menu_1668 | `_Base Library Menu Item 13` | Window > Symbol Libraries > Illuminate Flow Charts |  |  | ignored |
| menu_1669 | `_Base Library Menu Item 14` | Window > Symbol Libraries > Illuminate Org Charts |  |  | ignored |
| menu_1670 | `_Base Library Menu Item 15` | Window > Symbol Libraries > Illuminate Ribbons |  |  | ignored |
| menu_1671 | `_Base Library Menu Item 16` | Window > Symbol Libraries > Indigenous |  |  | ignored |
| menu_1672 | `_Base Library Menu Item 17` | Window > Symbol Libraries > Logo Elements |  |  | ignored |
| menu_1673 | `_Base Library Menu Item 18` | Window > Symbol Libraries > Mad Science |  |  | ignored |
| menu_1674 | `_Base Library Menu Item 19` | Window > Symbol Libraries > Maps |  |  | ignored |
| menu_1675 | `_Base Library Menu Item 20` | Window > Symbol Libraries > Mobile |  |  | ignored |
| menu_1676 | `_Base Library Menu Item 21` | Window > Symbol Libraries > Nature |  |  | ignored |
| menu_1677 | `_Base Library Menu Item 22` | Window > Symbol Libraries > Regal Vector Pack |  |  | ignored |
| menu_1678 | `_Base Library Menu Item 23` | Window > Symbol Libraries > Retro |  |  | ignored |
| menu_1679 | `_Base Library Menu Item 24` | Window > Symbol Libraries > Sushi |  |  | ignored |
| menu_1680 | `_Base Library Menu Item 25` | Window > Symbol Libraries > Tiki |  |  | ignored |
| menu_1681 | `_Base Library Menu Item 26` | Window > Symbol Libraries > Web Buttons and Bars |  |  | ignored |
| menu_1682 | `_Base Library Menu Item 27` | Window > Symbol Libraries > Web Icons |  |  | ignored |
| menu_1683 | `Adobe Symbol Palette Plugin Other libraries menu item` | Window > Symbol Libraries > Other Library... |  |  |  |
