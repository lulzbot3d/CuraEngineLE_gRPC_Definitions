pub mod cura {
    pub mod plugins {
        pub mod v1 {
            tonic::include_proto!("cura.plugins.v1");
        }
        pub mod slots {
            pub mod overhang_areas {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.overhang_areas.v1");
                }
            }
            pub mod comb {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.comb.v1");
                }
            }
            pub mod platform_adhesion {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.platform_adhesion.v1");
                }
            }
            pub mod postprocess {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.postprocess.v1");
                }
            }
            pub mod skin {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.skin.v1");
                }
            }
            pub mod slice {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.slice.v1");
                }
            }
            pub mod simplify {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.simplify.v1");
                }
            }
            pub mod infill {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.infill.v1");
                }
            }
            pub mod wall_tool_paths {
                pub mod v1 {
                    tonic::include_proto!("cura.plugins.slots.wall_toolpaths.v1");
                }
            }
        }
    }
}
