use std::io::Result;

fn main() -> Result<()> {
    // Compile the proto files
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(
            &[
                "cura/plugins/overhang_areas/v1/overhang_areas.proto",
                "cura/plugins/comb/v1/comb.proto",
                "cura/plugins/infill/v1/infill.proto",
                "cura/plugins/platform_adhesion/v1/platform_adhesion.proto",
                "cura/plugins/postprocessing/v1/postprocess.proto",
                "cura/plugins/simplify/v1/simplify.proto",
                "cura/plugins/skin/v1/skin.proto",
                "cura/plugins/slice/v1/slice.proto",
                "cura/plugins/v1/broadcast_slots.proto",
                "cura/plugins/v1/cura.proto",
                "cura/plugins/v1/layers.proto",
                "cura/plugins/v1/mesh.proto",
                "cura/plugins/v1/polygons.proto",
                "cura/plugins/v1/slot_id.proto",
                "cura/plugins/v1/toolpaths.proto",
                "cura/plugins/wall_toolpaths/v1/wall_toolpaths.proto",
            ],
            &["./"],
        )?;

    Ok(())
}
