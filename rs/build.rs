use glob::glob;
use std::io::Result;

fn main() -> Result<()> {
    let proto_files = glob("**/*.proto")
        .expect("Failed to read glob pattern")
        .into_iter()
        .map(|p| p.ok().expect("Failed to read glob pattern"))
        .collect::<Vec<_>>();

    // Compile the proto files
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(&proto_files, &["./"])?;

    Ok(())
}
