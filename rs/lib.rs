pub mod cura {
    pub mod plugins {
        pub mod v0 {
            tonic::include_proto!("cura.plugins.v0");
        }
        pub mod slots {
            pub mod overhang_areas {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.overhang_areas.v0");
                }
            }
            pub mod comb {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.comb.v0");
                }
            }
            pub mod platform_adhesion {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.platform_adhesion.v0");
                }
            }
            pub mod postprocess {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.postprocess.v0");
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
                    tonic::include_proto!("cura.plugins.slots.simplify.v0");
                }
            }
            pub mod infill {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.infill.v0");
                }
            }
            pub mod wall_tool_paths {
                pub mod v0 {
                    tonic::include_proto!("cura.plugins.slots.wall_toolpaths.v0");
                }
            }
        }
    }
}
