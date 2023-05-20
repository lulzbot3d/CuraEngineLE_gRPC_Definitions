use std::io::Result;

fn main() -> Result<()> {
    // Compile the proto files
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(
            &[
                "broadcast_slots.proto",
                "comb.proto",
                "infill.proto",
                "layers.proto",
                "overhang_areas.proto",
                "platform_adhesion.proto",
                "settings.proto",
                "skin.proto",
                "slice.proto",
                "tool_paths.proto",
                "wall_tool_paths.proto",
            ],
            &["./"],
        )?;

    Ok(())
}
