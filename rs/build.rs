use std::io::Result;

fn main() -> Result<()> {
    // Compile the proto files
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(
            &[
                "plugin.proto",
                "polygons.proto",
                "postprocess.proto",
                "simplify.proto",
            ],
            &["./"],
        )?;

    Ok(())
}
