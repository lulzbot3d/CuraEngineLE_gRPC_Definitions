use tonic::{transport::Server, Request, Response, Status};

use curaengine_grpc_defintions::plugin_server::{Plugin, PluginServer};
use curaengine_grpc_defintions::{PluginRequest, PluginResponse};

use curaengine_grpc_defintions::simplify_server::{Simplify, SimplifyServer};
use curaengine_grpc_defintions::{SimplifyRequest, SimplifyResponse};

use curaengine_grpc_defintions::postprocess_server::{Postprocess, PostprocessServer};
use curaengine_grpc_defintions::{PostprocessRequest, PostprocessResponse};

#[derive(Default)]
struct PluginServicer {}

#[tonic::async_trait]
impl Plugin for PluginServicer {
    async fn identify(
        &self,
        request: Request<PluginRequest>,
    ) -> Result<Response<PluginResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());
        Result::Ok(Response::new(PluginResponse {
            plugin_hash: "1234567890".to_string(),
            version: "0.0.1".to_string(),
        }))
    }
}

#[derive(Default)]
struct SimplifyServicer {}

#[tonic::async_trait]
impl Simplify for SimplifyServicer {
    async fn simplify(
        &self,
        request: Request<SimplifyRequest>,
    ) -> Result<Response<SimplifyResponse>, Status> {
        Result::Ok(Response::new(SimplifyResponse {
            polygons: request.into_inner().polygons,
        }))
    }
}

#[derive(Default)]
struct PostprocessServicer {}

#[tonic::async_trait]
impl Postprocess for PostprocessServicer {
    async fn postprocess(
        &self,
        request: Request<PostprocessRequest>,
    ) -> Result<Response<PostprocessResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());
        println!("gcode word: {}", request.into_inner().gcode_word);
        Result::Ok(Response::new(PostprocessResponse {
            gcode_word: "Hello World".to_string(),
        }))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let address: std::net::SocketAddr = "[::]:5555".parse()?;
    let version = env!("CARGO_PKG_VERSION").to_string();
    println!("curaengine-grpc-server v{version} listening on {address}");

    Server::builder()
        .add_service(PluginServer::new(PluginServicer::default()))
        .add_service(SimplifyServer::new(SimplifyServicer::default()))
        .add_service(PostprocessServer::new(PostprocessServicer::default()))
        .serve(address)
        .await?;

    Ok(())
}
