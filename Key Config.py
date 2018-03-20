import bpy
import os

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)

wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map Screen
km = kc.keymaps.new('Screen', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('render.render_still', 'F12', 'PRESS')
kmi = km.keymap_items.new('render.render_animation', 'F12', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('render.render_view', 'F12', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.marker_jump', 'Q', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'next', False)
kmi = km.keymap_items.new('screen.marker_jump', 'W', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'next', True)
kmi = km.keymap_items.new('screen.animation_step', 'TIMER0', 'ANY', any=True)
kmi = km.keymap_items.new('screen.region_blend', 'TIMERREGION', 'ANY', any=True)
kmi = km.keymap_items.new('screen.screen_set', 'RIGHT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', 1)
kmi = km.keymap_items.new('screen.screen_set', 'LEFT_ARROW', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'delta', -1)
kmi = km.keymap_items.new('screen.screen_full_area', 'UP_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'DOWN_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'SPACE', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'F10', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'use_hide_panels', True)
kmi = km.keymap_items.new('screen.screenshot', 'F3', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screencast', 'F3', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.space_context_cycle', 'TAB', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'direction', 'NEXT')
kmi = km.keymap_items.new('screen.space_context_cycle', 'TAB', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'direction', 'PREV')
kmi = km.keymap_items.new('screen.region_quadview', 'Q', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.repeat_history', 'F3', 'PRESS')
kmi = km.keymap_items.new('screen.repeat_last', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.region_flip', 'F5', 'PRESS')
kmi = km.keymap_items.new('screen.redo_last', 'F6', 'PRESS')
kmi = km.keymap_items.new('script.reload', 'F8', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'RET', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'NUMPAD_ENTER', 'PRESS')
kmi = km.keymap_items.new('file.cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('ed.undo', 'Z', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('ed.redo', 'Z', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('ed.undo_history', 'Z', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS')
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'animation', True)
kmi_props_setattr(kmi.properties, 'use_viewport', True)
kmi = km.keymap_items.new('render.view_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('render.view_show', 'F11', 'PRESS')
kmi = km.keymap_items.new('render.play_rendered_anim', 'F11', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.userpref_show', 'U', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.repeat_history', 'BUTTON5MOUSE', 'PRESS')

# Map Sculpt
km = kc.keymaps.new('Sculpt', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('alm.sculpt_menu_call', 'SPACE', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_sv3_brush_options')
kmi = km.keymap_items.new('sculpt.brush_stroke', 'LEFTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'NORMAL')
kmi = km.keymap_items.new('sculpt.brush_stroke', 'LEFTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'INVERT')
kmi = km.keymap_items.new('sculpt.brush_stroke', 'LEFTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'SMOOTH')
kmi = km.keymap_items.new('paint.hide_show', 'H', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'action', 'SHOW')
kmi_props_setattr(kmi.properties, 'area', 'INSIDE')
kmi = km.keymap_items.new('paint.hide_show', 'H', 'PRESS')
kmi_props_setattr(kmi.properties, 'action', 'HIDE')
kmi_props_setattr(kmi.properties, 'area', 'INSIDE')
kmi = km.keymap_items.new('paint.hide_show', 'H', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'action', 'SHOW')
kmi_props_setattr(kmi.properties, 'area', 'ALL')
kmi = km.keymap_items.new('object.subdivision_set', 'ZERO', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 0)
kmi = km.keymap_items.new('object.subdivision_set', 'ONE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 1)
kmi = km.keymap_items.new('object.subdivision_set', 'TWO', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 2)
kmi = km.keymap_items.new('object.subdivision_set', 'THREE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 3)
kmi = km.keymap_items.new('object.subdivision_set', 'FOUR', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 4)
kmi = km.keymap_items.new('object.subdivision_set', 'FIVE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 5)
kmi = km.keymap_items.new('paint.mask_flood_fill', 'M', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'mode', 'VALUE')
kmi_props_setattr(kmi.properties, 'value', 0.0)
kmi = km.keymap_items.new('paint.mask_flood_fill', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'INVERT')
kmi = km.keymap_items.new('paint.mask_lasso_gesture', 'LEFTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('sculpt.dynamic_topology_toggle', 'D', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sculpt.set_detail_size', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('object.subdivision_set', 'PAGE_UP', 'PRESS')
kmi_props_setattr(kmi.properties, 'level', 1)
kmi_props_setattr(kmi.properties, 'relative', True)
kmi = km.keymap_items.new('object.subdivision_set', 'PAGE_DOWN', 'PRESS')
kmi_props_setattr(kmi.properties, 'level', -1)
kmi_props_setattr(kmi.properties, 'relative', True)
kmi = km.keymap_items.new('brush.active_index_set', 'ONE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 0)
kmi = km.keymap_items.new('brush.active_index_set', 'TWO', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 1)
kmi = km.keymap_items.new('brush.active_index_set', 'THREE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 2)
kmi = km.keymap_items.new('brush.active_index_set', 'FOUR', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 3)
kmi = km.keymap_items.new('brush.active_index_set', 'FIVE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 4)
kmi = km.keymap_items.new('brush.active_index_set', 'SIX', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 5)
kmi = km.keymap_items.new('brush.active_index_set', 'SEVEN', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 6)
kmi = km.keymap_items.new('brush.active_index_set', 'EIGHT', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 7)
kmi = km.keymap_items.new('brush.active_index_set', 'NINE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 8)
kmi = km.keymap_items.new('brush.active_index_set', 'ZERO', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 9)
kmi = km.keymap_items.new('brush.active_index_set', 'ONE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 10)
kmi = km.keymap_items.new('brush.active_index_set', 'TWO', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 11)
kmi = km.keymap_items.new('brush.active_index_set', 'THREE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 12)
kmi = km.keymap_items.new('brush.active_index_set', 'FOUR', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 13)
kmi = km.keymap_items.new('brush.active_index_set', 'FIVE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 14)
kmi = km.keymap_items.new('brush.active_index_set', 'SIX', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 15)
kmi = km.keymap_items.new('brush.active_index_set', 'SEVEN', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 16)
kmi = km.keymap_items.new('brush.active_index_set', 'EIGHT', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 17)
kmi = km.keymap_items.new('brush.active_index_set', 'NINE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 18)
kmi = km.keymap_items.new('brush.active_index_set', 'ZERO', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'sculpt')
kmi_props_setattr(kmi.properties, 'index', 19)
kmi = km.keymap_items.new('brush.scale_size', 'LEFT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'scalar', 0.8999999761581421)
kmi = km.keymap_items.new('brush.scale_size', 'RIGHT_BRACKET', 'PRESS')
kmi_props_setattr(kmi.properties, 'scalar', 1.1111111640930176)
kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.size')
kmi_props_setattr(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
kmi_props_setattr(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
kmi_props_setattr(kmi.properties, 'fill_color_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', '')
kmi_props_setattr(kmi.properties, 'zoom_path', '')
kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
kmi_props_setattr(kmi.properties, 'secondary_tex', False)
kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.strength')
kmi_props_setattr(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
kmi_props_setattr(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
kmi_props_setattr(kmi.properties, 'fill_color_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', '')
kmi_props_setattr(kmi.properties, 'zoom_path', '')
kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
kmi_props_setattr(kmi.properties, 'secondary_tex', False)
kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.texture_slot.angle')
kmi_props_setattr(kmi.properties, 'data_path_secondary', '')
kmi_props_setattr(kmi.properties, 'use_secondary', '')
kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
kmi_props_setattr(kmi.properties, 'fill_color_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_path', '')
kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', '')
kmi_props_setattr(kmi.properties, 'zoom_path', '')
kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
kmi_props_setattr(kmi.properties, 'secondary_tex', False)
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'mode', 'TRANSLATION')
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'mode', 'SCALE')
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'mode', 'ROTATION')
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'mode', 'TRANSLATION')
kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'mode', 'SCALE')
kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'mode', 'ROTATION')
kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
kmi = km.keymap_items.new('paint.brush_select', 'X', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'DRAW')
kmi = km.keymap_items.new('paint.brush_select', 'S', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'SMOOTH')
kmi = km.keymap_items.new('paint.brush_select', 'P', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'PINCH')
kmi = km.keymap_items.new('paint.brush_select', 'I', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'INFLATE')
kmi = km.keymap_items.new('paint.brush_select', 'G', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'GRAB')
kmi = km.keymap_items.new('paint.brush_select', 'L', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'LAYER')
kmi = km.keymap_items.new('paint.brush_select', 'T', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'FLATTEN')
kmi = km.keymap_items.new('paint.brush_select', 'C', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'CLAY')
kmi = km.keymap_items.new('paint.brush_select', 'C', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'CREASE')
kmi = km.keymap_items.new('paint.brush_select', 'K', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'SNAKE_HOOK')
kmi = km.keymap_items.new('paint.brush_select', 'M', 'PRESS')
kmi_props_setattr(kmi.properties, 'paint_mode', 'SCULPT')
kmi_props_setattr(kmi.properties, 'sculpt_tool', 'MASK')
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi_props_setattr(kmi.properties, 'create_missing', True)
kmi = km.keymap_items.new('wm.context_menu_enum', 'E', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.sculpt.brush.stroke_method')
kmi = km.keymap_items.new('wm.context_toggle', 'S', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.sculpt.brush.use_smooth_stroke')
kmi = km.keymap_items.new('wm.call_menu', 'R', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_angle_control')
kmi = km.keymap_items.new('brush.scale_size', 'WHEELUPMOUSE', 'ANY', alt=True)
kmi_props_setattr(kmi.properties, 'scalar', 1.100000023841858)
kmi = km.keymap_items.new('brush.scale_size', 'WHEELDOWNMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'scalar', 0.8999999761581421)

# Map Mesh
km = kc.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('mesh.f2', 'F', 'PRESS')
kmi = km.keymap_items.new('mesh.loopcut_slide', 'R', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.offset_edge_loops_slide', 'R', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('mesh.inset', 'I', 'PRESS')
kmi = km.keymap_items.new('mesh.poke', 'P', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.bevel', 'B', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'vertex_only', False)
kmi = km.keymap_items.new('mesh.bevel', 'B', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'vertex_only', True)
kmi = km.keymap_items.new('mesh.loop_select', 'SELECTMOUSE', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi = km.keymap_items.new('mesh.loop_select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi = km.keymap_items.new('mesh.edgering_select', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi = km.keymap_items.new('mesh.edgering_select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi = km.keymap_items.new('mesh.shortest_path_pick', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'use_fill', False)
kmi = km.keymap_items.new('mesh.shortest_path_pick', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'use_fill', True)
kmi = km.keymap_items.new('mesh.select_all', 'A', 'PRESS')
kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')
kmi = km.keymap_items.new('mesh.select_all', 'I', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'action', 'INVERT')
kmi = km.keymap_items.new('mesh.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_next_item', 'NUMPAD_PLUS', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('mesh.select_prev_item', 'NUMPAD_MINUS', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('mesh.select_non_manifold', 'M', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('mesh.select_linked', 'L', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_linked_pick', 'L', 'PRESS')
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi = km.keymap_items.new('mesh.select_linked_pick', 'L', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'deselect', True)
kmi = km.keymap_items.new('mesh.faces_select_linked_flat', 'F', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('wm.call_menu', 'G', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_select_similar')
kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_select_mode')
kmi = km.keymap_items.new('mesh.hide', 'H', 'PRESS')
kmi_props_setattr(kmi.properties, 'unselected', False)
kmi = km.keymap_items.new('mesh.hide', 'H', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'unselected', True)
kmi = km.keymap_items.new('mesh.reveal', 'H', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.normals_make_consistent', 'N', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'inside', False)
kmi = km.keymap_items.new('mesh.normals_make_consistent', 'N', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'inside', True)
kmi = km.keymap_items.new('view3d.edit_mesh_extrude_move_normal', 'E', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_extrude')
kmi = km.keymap_items.new('transform.edge_crease', 'E', 'PRESS', shift=True)
kmi = km.keymap_items.new('mesh.spin', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.fill', 'F', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.beautify_fill', 'F', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('mesh.quads_convert_to_tris', 'T', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'quad_method', 'BEAUTY')
kmi_props_setattr(kmi.properties, 'ngon_method', 'BEAUTY')
kmi = km.keymap_items.new('mesh.quads_convert_to_tris', 'T', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'quad_method', 'FIXED')
kmi_props_setattr(kmi.properties, 'ngon_method', 'CLIP')
kmi = km.keymap_items.new('mesh.tris_convert_to_quads', 'J', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.rip_move', 'V', 'PRESS')
kmi = km.keymap_items.new('mesh.rip_move_fill', 'V', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.rip_edge_move', 'D', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.merge', 'M', 'PRESS', alt=True)
kmi = km.keymap_items.new('transform.shrink_fatten', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.edge_face_add', 'F', 'PRESS')
kmi = km.keymap_items.new('mesh.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'name', 'INFO_MT_mesh_add')
kmi = km.keymap_items.new('mesh.separate', 'P', 'PRESS')
kmi = km.keymap_items.new('mesh.split', 'Y', 'PRESS')
kmi = km.keymap_items.new('mesh.vert_connect_path', 'J', 'PRESS')
kmi = km.keymap_items.new('transform.vert_slide', 'V', 'PRESS', shift=True)
kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'ACTIONMOUSE', 'CLICK', ctrl=True)
kmi_props_setattr(kmi.properties, 'rotate_source', True)
kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'ACTIONMOUSE', 'CLICK', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'rotate_source', False)
kmi = km.keymap_items.new('wm.call_menu', 'X', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_delete')
kmi = km.keymap_items.new('wm.call_menu', 'DEL', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_delete')
kmi = km.keymap_items.new('mesh.dissolve_mode', 'X', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.dissolve_mode', 'DEL', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.knife_tool', 'K', 'PRESS')
kmi_props_setattr(kmi.properties, 'use_occlude_geometry', True)
kmi_props_setattr(kmi.properties, 'only_selected', False)
kmi = km.keymap_items.new('mesh.knife_tool', 'K', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'use_occlude_geometry', False)
kmi_props_setattr(kmi.properties, 'only_selected', True)
kmi = km.keymap_items.new('object.vertex_parent_set', 'P', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_specials')
kmi = km.keymap_items.new('wm.call_menu', 'F', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_faces')
kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_edges')
kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_vertices')
kmi = km.keymap_items.new('wm.call_menu', 'H', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_hook')
kmi = km.keymap_items.new('wm.call_menu', 'U', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_uv_map')
kmi = km.keymap_items.new('wm.call_menu', 'G', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_vertex_group')
kmi = km.keymap_items.new('object.subdivision_set', 'ZERO', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 0)
kmi = km.keymap_items.new('object.subdivision_set', 'ONE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 1)
kmi = km.keymap_items.new('object.subdivision_set', 'TWO', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 2)
kmi = km.keymap_items.new('object.subdivision_set', 'THREE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 3)
kmi = km.keymap_items.new('object.subdivision_set', 'FOUR', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 4)
kmi = km.keymap_items.new('object.subdivision_set', 'FIVE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'level', 5)
kmi = km.keymap_items.new('wm.context_cycle_enum', 'O', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.proportional_edit_falloff')
kmi_props_setattr(kmi.properties, 'wrap', True)
kmi = km.keymap_items.new('wm.context_toggle_enum', 'O', 'PRESS')
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.proportional_edit')
kmi_props_setattr(kmi.properties, 'value_1', 'DISABLED')
kmi_props_setattr(kmi.properties, 'value_2', 'ENABLED')
kmi = km.keymap_items.new('wm.context_toggle_enum', 'O', 'PRESS', alt=True)
kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.proportional_edit')
kmi_props_setattr(kmi.properties, 'value_1', 'DISABLED')
kmi_props_setattr(kmi.properties, 'value_2', 'CONNECTED')
kmi = km.keymap_items.new('wm.call_menu', 'BUTTON4MOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_edit_mesh_select_mode')
