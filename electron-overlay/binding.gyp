{
    "targets": [
        {
            "target_name": "electron_overlay",
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
            "include_dirs": [
                "./src",
                "./src/3rd",
                "./src/3rd/boost",
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "sources": [
                "./src/ipc/tinyipc.h",
                "./src/ipc/ipcmsg.h",
                "./src/ipc/ipclink.h",
                "./src/ipc/ipclink.cc",
                "./src/ipc/ipccenter.h",
                "./src/ipc/ipccenter.cc",
                "./src/utils.hpp",
                "./src/overlay.hpp",
                "./src/overlay.cc",
                "./src/windll.hpp",
                "./src/node_async_call.h",
                "./src/node_async_call.cc",
                "./src/3rd/nlohmann/json.hpp",
                "./src/message/gmessage.hpp",
                "./src/n-utils.hpp",
                "./src/main.cc"
            ],
            "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS", "UNICODE"],
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ],
            "conditions": [
                [
                    "OS=='win'", {
                        "defines": [
                            "_UNICODE",
                            "_WIN32_WINNT=0x0601"
                        ],
                        "configurations": {
                            "Release": {
                                "msvs_settings": {
                                    "VCCLCompilerTool": {
                                        "ExceptionHandling": 1,
                                    }
                                }
                            },
                            "Debug": {
                                "msvs_settings": {
                                    "VCCLCompilerTool": {
                                        "ExceptionHandling": 1,
                                    }
                                }
                            }
                        }
                    }
                ]
            ]
        }
    ]
}
