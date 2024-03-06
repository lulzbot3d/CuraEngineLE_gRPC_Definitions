pub mod v0 {
    tonic::include_proto!("cura.plugins.v0");
}
pub mod slots {
    pub mod broadcast {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.slots.broadcast.v0");
        }
    }
    pub mod handshake {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.slots.handshake.v0");
        }
    }
    pub mod infill {
        pub mod v0 {
            pub mod generate {
                tonic::include_proto!("cura.plugins.slots.infill.v0.generate");
            }
            pub mod modify {
                tonic::include_proto!("cura.plugins.slots.infill.v0.modify");
            }
        }
    }
    pub mod gcode_paths {
        pub mod v0 {
            pub mod modify {
                tonic::include_proto!("cura.plugins.slots.gcode_paths.v0.modify");
            }
        }
    }
    pub mod postprocess {
        pub mod v0 {
            pub mod modify {
                tonic::include_proto!("cura.plugins.slots.postprocess.v0.modify");
            }
        }
    }
    pub mod skin {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.slots.skin.v0");
        }
    }
    pub mod slice {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.slots.slice.v0");
        }
    }
    pub mod simplify {
        pub mod v0 {
            pub mod modify {
                tonic::include_proto!("cura.plugins.slots.simplify.v0.modify");
            }
        }
    }
    pub mod wall_tool_paths {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.slots.wall_toolpaths.v0");
        }
    }
}
