[app]

# (str) Title of your application
title = UOK FAQ Bot

# (str) Package name
package.name = faqbot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.uok

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (int) Target Android API, should not be below 21. 33 is the latest as of 2023
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. Defaults to 21
android.ndk_api = 21

# (bool) Enable AndroidX (macro for setting android.build_tools_gradle_version to 3.6.4 or higher)
android.enable_androidx = True

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Override log level (0-2)
# 0 = INFO, 1 = DEBUG, 2 = ERROR
log_level = 2

# (bool) Display splash screen
android.splash = True

# (str) Filename of the application icon
android.icon.filename = %(source.dir)s/icon.png

# (str) Where to deploy the application
android.deploy_extras = 

# (str) Android entry point, default is ok for Kivy-based Apps
android.entrypoint = org.kivy.android.PythonActivity

# (str) The Android theme to use for the application
android.apptheme = @android:style/Theme.NoTitleBar

# (list) Gradle dependencies to add
android.gradle_dependencies = 

# (bool) Enable copying target architecture instead of compiler's default
build.copy_target_arch = False

# (list) Recipe to build
android.add_compile_options = 

# (str) The directory to join the application with
android.join_app_dir = 

# (str) Key alias for signing the debug APK
android.debug.keyalias = androiddebugkey

# (str) Password for the debug key alias
android.debug.keypass = android

# (str) Password for the root key alias
android.debug.storepass = android

# (bool) Disable the default backup rules
android.backup_rules = False

# (str) Presplash color (for new android tooling)
android.presplash_color = #FFFFFF

# (bool) Show splash screen for Android v4
android.presplash_lottie = False

# (str) Filename of the presplash image
android.presplash.filename = %(source.dir)s/splash.png

# (str) Name for the icon which will appear in the notification panel
android.notch %= app

# (str) Path to the full notifiation icon
android.notification_icon = %(source.dir)s/notification_icon.png

# (str) Activity name for the full notifiation icon
android.notification_activity = org.kivy.android.PythonActivity

# (str) Application package name
android.package.application_id = org.uok.faqbot

# (str) Full path to the Android SDK
#android.sdk_path = 

# (str) Full path to the Android NDK
#android.ndk_path = 

# (str) Android NDK version to use
#android.ndk_version = 

# (str) Android SDK version to use
#android.sdk_version = 

# (str) Android build tools version to use
#android.build_tools_version = 

# (str) Android gradle plugin version to use
#android.gradle_plugin_version = 

# (str) Android build.gradle version to use
#android.build_gradle_version = 

# (str) Android target SDK version to use
#android.target_sdk_version = 

# (str) Android compile SDK version to use
#android.compile_sdk_version = 

# (list) Python modules to install
android.add_compile_options = --add-python-module=urllib3

requirements = python3, kivy==2.2.1, requests, urllib3, plyer

# (str) Garden package to install
# garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) URL schemes that this app can handle (e.g. webcomic-reader-api://entry/)
# export.aars = 

# (bool) Indicate that the application should be fullscreen
fullscreen = 0

# (string) Presplash background color (for new android tooling)
# Valid formats are: #RRGGBB, #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# presplash_color = #FFFFFF

# (list) Permissions
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,ACCESS_FINE_LOCATION,VIBRATE

# (str) Native opponent identifier for Google Play In-app Billing
# android.native_opponent_id = 

# (str) Android additional intent options
# android.additional_options = 

# (str) Android additional manifest options
# android.manifest_options = 

# (str) Android additional gradle options
# android.gradle_options = 

# (str) Android additional aar options
# android.aar_options = 

# (str) Android additional java options
# android.java_options = 

# (str) Android additional assets options
# android.assets_options = 

# (str) Android additional res options
# android.res_options = 

# (str) Android additional libs options
# android.libs_options = 

# (str) Android additional jni options
# android.jni_options = 

# (str) Android additional src options
# android.src_options = 

# (str) Android additional build options
# android.build_options = 

# (str) Android additional install options
# android.install_options = 

# (str) Android additional uninstall options
# android.uninstall_options = 

# (str) Android additional update options
# android.update_options = 

# (str) Android additional clean options
# android.clean_options = 

# (str) Android additional distclean options
# android.distclean_options = 

# (str) Android additional rebuild options
# android.rebuild_options = 

# (str) Android additional debug options
# android.debug_options = 

# (str) Android additional release options
# android.release_options = 

# (str) Android additional buildozer options
# android.buildozer_options = 

# (str) Android additional python-for-android options
# android.p4a_options = 

# (str) Android additional cython options
# android.cython_options = 

# (str) Android additional apk options
# android.apk_options = 

# (str) Android additional buildozer apk options
# android.buildozer_apk_options = 

# (str) Android additional p4a apk options
# android.p4a_apk_options = 

# (str) Android additional gradle apk options
# android.gradle_apk_options = 

# (str) Android additional build tools apk options
# android.build_tools_apk_options = 

# (str) Android additional sdk apk options
# android.sdk_apk_options = 

# (str) Android additional ndk apk options
# android.ndk_apk_options = 

# (str) Android additional native apk options
# android.native_apk_options = 

# (str) Android additional python apk options
# android.python_apk_options = 

# (str) Android additional kivy apk options
# android.kivy_apk_options = 

# (str) Android additional app apk options
# android.app_apk_options = 

# (str) Android additional project apk options
# android.project_apk_options = 

# (str) Android additional module apk options
# android.module_apk_options = 

# (str) Android additional recipe apk options
# android.recipe_apk_options = 

# (str) Android additional build apk options
# android.build_apk_options = 

# (str) Android additional package apk options
# android.package_apk_options = 

# (str) Android additional sign apk options
# android.sign_apk_options = 

# (str) Android additional zipalign apk options
# android.zipalign_apk_options = 

# (str) Android additional jarsigner apk options
# android.jarsigner_apk_options = 

# (str) Android additional aapt apk options
# android.aapt_apk_options = 

# (str) Android additional dx apk options
# android.dx_apk_options = 

# (str) Android additional proguard apk options
# android.proguard_apk_options = 

# (str) Android additional multidex apk options
# android.multidex_apk_options = 

# (str) Android additional instant apk options
# android.instant_apk_options = 

# (str) Android additional bundle apk options
# android.bundle_apk_options = 

# (str) Android additional universal apk options
# android.universal_apk_options = 

# (str) Android additional splits apk options
# android.splits_apk_options = 

# (str) Android additional abi apk options
# android.abi_apk_options = 

# (str) Android additional density apk options
# android.density_apk_options = 

# (str) Android additional locale apk options
# android.locale_apk_options = 

# (str) Android additional version apk options
# android.version_apk_options = 

# (str) Android additional versionCode apk options
# android.versioncode_apk_options = 

# (str) Android additional versionName apk options
# android.versionname_apk_options = 

# (str) Android additional applicationId apk options
# android.applicationid_apk_options = 

# (str) Android additional packageName apk options
# android.packagename_apk_options = 

# (str) Android additional package apk options
# android.package_apk_options = 

# (str) Android additional application apk options
# android.application_apk_options = 

# (str) Android additional activity apk options
# android.activity_apk_options = 

# (str) Android additional service apk options
# android.service_apk_options = 

# (str) Android additional receiver apk options
# android.receiver_apk_options = 

# (str) Android additional provider apk options
# android.provider_apk_options = 

# (str) Android additional intent apk options
# android.intent_apk_options = 

# (str) Android additional permission apk options
# android.permission_apk_options = 

# (str) Android additional uses-feature apk options
# android.uses_feature_apk_options = 

# (str) Android additional uses-library apk options
# android.uses_library_apk_options = 

# (str) Android additional supports-screens apk options
# android.supports_screens_apk_options = 

# (str) Android additional compatible-screens apk options
# android.compatible_screens_apk_options = 

# (str) Android additional large-destinations apk options
# android.large_destinations_apk_options = 

# (str) Android additional any-density apk options
# android.any_density_apk_options = 

# (str) Android additional normal-dpi apk options
# android.normal_dpi_apk_options = 

# (str) Android additional tvdpi apk options
# android.tvdpi_apk_options = 

# (str) Android additional hdpi apk options
# android.hdpi_apk_options = 

# (str) Android additional xhdpi apk options
# android.xhdpi_apk_options = 

# (str) Android additional xxhdpi apk options
# android.xxhdpi_apk_options = 

# (str) Android additional xxxhdpi apk options
# android.xxxhdpi_apk_options = 

# (str) Android additional nodpi apk options
# android.nodpi_apk_options = 

# (str) Android additional anydpi-v26 apk options
# android.anydpi_v26_apk_options = 

# (str) Android additional layout-land apk options
# android.layout_land_apk_options = 

# (str) Android additional layout-port apk options
# android.layout_port_apk_options = 

# (str) Android additional layout-sw320dp apk options
# android.layout_sw320dp_apk_options = 

# (str) Android additional layout-sw480dp apk options
# android.layout_sw480dp_apk_options = 

# (str) Android additional layout-sw600dp apk options
# android.layout_sw600dp_apk_options = 

# (str) Android additional layout-sw720dp apk options
# android.layout_sw720dp_apk_options = 

# (str) Android additional layout-w820dp apk options
# android.layout_w820dp_apk_options = 

# (str) Android additional layout-h820dp apk options
# android.layout_h820dp_apk_options = 

# (str) Android additional layout-xlarge apk options
# android.layout_xlarge_apk_options = 

# (str) Android additional layout-large apk options
# android.layout_large_apk_options = 

# (str) Android additional layout-normal apk options
# android.layout_normal_apk_options = 

# (str) Android additional layout-small apk options
# android.layout_small_apk_options = 

# (str) Android additional layout-ldpi apk options
# android.layout_ldpi_apk_options = 

# (str) Android additional layout-mdpi apk options
# android.layout_mdpi_apk_options = 

# (str) Android additional layout-tvdpi apk options
# android.layout_tvdpi_apk_options = 

# (str) Android additional layout-hdpi apk options
# android.layout_hdpi_apk_options = 

# (str) Android additional layout-xhdpi apk options
# android.layout_xhdpi_apk_options = 

# (str) Android additional layout-xxhdpi apk options
# android.layout_xxhdpi_apk_options = 

# (str) Android additional layout-xxxhdpi apk options
# android.layout_xxxhdpi_apk_options = 

# (str) Android additional layout-nodpi apk options
# android.layout_nodpi_apk_options = 

# (str) Android additional layout-anydpi-v26 apk options
# android.layout_anydpi_v26_apk_options = 

# (str) Android additional layout-land-small apk options
# android.layout_land_small_apk_options = 

# (str) Android additional layout-land-normal apk options
# android.layout_land_normal_apk_options = 

# (str) Android additional layout-land-large apk options
# android.layout_land_large_apk_options = 

# (str) Android additional layout-land-xlarge apk options
# android.layout_land_xlarge_apk_options = 

# (str) Android additional layout-port-small apk options
# android.layout_port_small_apk_options = 

# (str) Android additional layout-port-normal apk options
# android.layout_port_normal_apk_options = 

# (str) Android additional layout-port-large apk options
# android.layout_port_large_apk_options = 

# (str) Android additional layout-port-xlarge apk options
# android.layout_port_xlarge_apk_options = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = warning, 1 = yes, 2 = no)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = 

# (str) Path to build distribution artifacts, absolute or relative to spec file
# bin_dir = 

# (bool) For debug purpose, run the build sequence inside the build dir
build_in_container = False

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to python-for-android folder
# path_p4a = 

# (str) Path to kivy-ios folder
# path_kivy_ios = 

# (str) Path to sdl2 folder
# path_sdl2 = 

# (str) Path to pygame folder
# path_pygame = 

# (str) Path to kivy folder
# path_kivy = 

# (str) Path to python folder
# path_python = 

# (str) Path to cython folder
# path_cython = 

# (str) Path to cythonize folder
# path_cythonize = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets folder
# path_assets = 

# (str) Path to buildozer res folder
# path_res = 

# (str) Path to buildozer libs folder
# path_libs = 

# (str) Path to buildozer src folder
# path_src = 

# (str) Path to buildozer tmp folder
# path_tmp = 

# (str) Path to buildozer log folder
# path_log = 

# (str) Path to buildozer config folder
# path_config = 

# (str) Path to buildozer state folder
# path_state = 

# (str) Path to buildozer target folder
# path_target = 

# (str) Path to buildozer app folder
# path_app = 

# (str) Path to buildozer build folder
# path_build = 

# (str) Path to buildozer dist folder
# path_dist = 

# (str) Path to buildozer p4a folder
# path_p4a = 

# (str) Path to buildozer kivy folder
# path_kivy = 

# (str) Path to buildozer python folder
# path_python = 

# (str) Path to buildozer cython folder
# path_cython = 

# (str) Path to buildozer sdl2 folder
# path_sdl2 = 

# (str) Path to buildozer pygame folder
# path_pygame = 

# (str) Path to buildozer kivy-ios folder
# path_kivy_ios = 

# (str) Path to buildozer folder
# path_buildozer = 

# (str) Path to buildozer cache folder
# path_cache = 

# (str) Path to buildozer downloads folder
# path_downloads = 

# (str) Path to buildozer packages folder
# path_packages = 

# (str) Path to buildozer apk folder
# path_apk = 

# (str) Path to buildozer aar folder
# path_aar = 

# (str) Path to buildozer jar folder
# path_jar = 

# (str) Path to buildozer so folder
# path_so = 

# (str) Path to buildozer assets