from expand_font_data import \
    fsTypeData, \
    fontFamilyClassData, \
    unicodeRangeData, \
    macStyleData

def getFontData(font):
    font_data = {
        "familyName": font.familyname,
        "fondName": font.fondname,
        "fontName": font.fontname,
        "fullName": font.fullname,
        "weight": font.weight,

        "uniqueId": font.uniqueid,
        "version": font.version,
        "sfntRevision": {
            "raw": font.sfntRevision,
            "cooked": ("%.3f" % font.sfntRevision),
            "numeric": round(font.sfntRevision * 1000) / 1000,
        },

        "comment": font.comment,
        "copyright": font.copyright,
        "fontLog": font.fontlog,

        "macStyle": {
            "numeric": font.macstyle,
            "data": macStyleData(font.macstyle)
        },
        "familyClass": {
            "numeric": font.os2_family_class,
            "data": fontFamilyClassData(font.os2_family_class),
        },
        "fsType": {
            "numeric": font.os2_fstype,
            "data": fsTypeData(font.os2_fstype),
        },
        "styleMap": {
            "numeric": font.os2_stylemap,
        },
        "panose": {
            "numeric": font.os2_panose,
        },
        "os2Weight": {
            "numeric": font.os2_weight,
        },
        "os2Width": {
            "numeric": font.os2_width,
        },

        "metrics": {
            "ascent": font.ascent,
            "capHeight": font.capHeight,
            "descent": font.descent,
            "designSize": font.design_size,
            "em": font.em,
            "italicAngle": font.italicangle,
            "underlinePos": font.upos,
            "underlineWidth": font.uwidth,
            "exHeight": font.xHeight,
        },
        "hheaMetrics": {
            "ascent": font.hhea_ascent,
            "ascentAdd": font.hhea_ascent_add,
            "descent": font.hhea_descent,
            "descentAdd": font.hhea_descent_add,
            "linegap": font.hhea_linegap,
        },
        "os2Metrics": {
            "strikeYPos": font.os2_strikeypos,
            "strikeYSize": font.os2_strikeysize,
            "subXOff": font.os2_subxoff,
            "subXSize": font.os2_subxsize,
            "subYOff": font.os2_subyoff,
            "subYSize": font.os2_subysize,
            "supXOff": font.os2_supxoff,
            "supXSize": font.os2_supxsize,
            "supYOff": font.os2_supyoff,
            "supYSize": font.os2_supysize,
        },
        "useTypoMetrics": font.os2_use_typo_metrics,
        "typoMetrics": {
            "ascent": font.os2_typoascent,
            "ascentAdd": font.os2_typoascent_add,
            "descent": font.os2_typodescent,
            "descentAdd": font.os2_typodescent_add,
            "linegap": font.os2_typolinegap,
        },
        "winMetrics": {
            "ascent": font.os2_winascent,
            "ascentAdd": font.os2_winascent_add,
            "descent": font.os2_windescent,
            "descentAdd": font.os2_windescent_add,
        },
        "vhea": {
            "linegap": font.vhea_linegap,
        },

        "isCid": font.is_cid,
        "cid": {
            "copyright": font.cidcopyright,
            "familyName": font.cidfamilyname,
            "fontName": font.cidfontname,
            "fullName": font.cidfullname,
            "ordering": font.cidordering,
            "registry": font.cidregistry,
            "subfont": font.cidsubfont,
            "subfontCnt": font.cidsubfontcnt,
            "subfontNames": font.cidsubfontnames,
            "supplement": font.cidsupplement,
            "version": font.cidversion,
            "weight": font.cidweight,
        },

        "encoding": font.encoding,
        "hasVMetrics": font.hasvmetrics,
        "headOptimizedForCleartype": font.head_optimized_for_cleartype,
        "horizontalBaseline": font.horizontalBaseline,
        "isQuadratic": font.is_quadratic,
        "onlyBitmaps": font.onlybitmaps,
        "codepages": font.os2_codepages,
        "unicodeRanges": {
            "raw": font.os2_unicoderanges,
            "repr": repr(font.os2_unicoderanges),
            "ranges": unicodeRangeData(font.os2_unicoderanges),
        },
        "os2Vendor": font.os2_vendor,
        "os2Version": font.os2_version, # OS/2 table version number
        "os2WeightWidthSlopeOnly": font.os2_weight_width_slope_only,
        "isStrokedFont": font.strokedfont,
        "strokeWidth": font.strokewidth,
        "verticalBaseline": font.verticalBaseline,
        "verticalOrigin": font.vertical_origin,
        "woffMajor": font.woffMajor,
        "woffMinor": font.woffMinor,
        "woffMetadata": font.woffMetadata,
        # "activeLayer": font.activeLayer,
        # "bitmapSizes": font.bitmapSizes,
        # "changed": font.changed,
        # "cvt": font.cvt, # not JSON serializable
        # "default_base_filename": font.default_base_filename,
        # "gasp": font.gasp,
        # "gasp_version": font.gasp_version,
        # "gpos_lookups": font.gpos_lookups,
        # "gsub_lookups": font.gsub_lookups,
        # "guide": font.guide,
        # "isnew": font.isnew,
        # "layer_cnt": font.layer_cnt,
        # "layers": font.layers,
        # "loadState": font.loadState,
        # "maxp_FDEFs": font.maxp_FDEFs,
        # "maxp_IDEFs": font.maxp_IDEFs,
        # "maxp_maxStackDepth": font.maxp_maxStackDepth,
        # "maxp_storageCnt": font.maxp_storageCnt,
        # "maxp_twilightPtCnt": font.maxp_twilightPtCnt,
        # "maxp_zones": font.maxp_zones,
        # "multilayer": font.multilayer,
        # "path": font.path,
        # "persistent": font.persistent,
        # "math": font.math,
        # "private": font.private,
        # "privateState": font.privateState,
        # "selection": font.selection,
        # "sfd_path": font.sfd_path,
        # "sfnt_names": font.sfnt_names,
        # "size_feature": font.size_feature,
        # "temporary": font.temporary,
        # "texparameters": font.texparameters,
        # "userdata": font.userdata,
    }
    return font_data
