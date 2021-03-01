Pod::Spec.new do |s|


  s.name         = "LADebug"
  s.version  = "0.0.2"
  s.summary      = "LADebug Source."

  s.description  = <<-DESC
                   LADebug Source description
                   DESC
  s.source = { :git => "git@gitlab.alibaba-inc.com:lazada-ios/LADebug.git", :branch => "master"  }

  s.homepage     = "http://gitlab.alibaba-inc.com/lazada-ios/LADebug"
  s.license = {
    :type => 'Copyright',
    :text => <<-LICENSE
           Alibaba-INC copyright
    LICENSE
  }

  s.author       = { "码猴" => "mahou.wy@alibaba-inc.com" }

  s.platform     = :ios, "8.0"

  s.source_files = 'LADebug/**/*.{swift,h,m}'  
  s.resources = "LADebug/**/*.{xib,plist}"
  s.exclude_files = "LADebug/**/Info.plist"
  s.requires_arc = true
  s.dependency 'ATSDK'
  s.dependency 'LAUIKit'
  s.dependency 'ZCache'
  s.dependency 'TBUniversalCategory'
  s.dependency 'AliIdentifier'
  s.dependency 'LAMacroConfig'
  s.dependency 'AliNavigator'
  s.dependency 'AliURLRouter'
  s.dependency 'NetworkSDK'
  s.dependency 'LAMainClient'
  s.dependency 'WXDevtool'
  s.dependency 'WeexAnalyzer'
  s.dependency 'LAUtility'
  s.dependency 'LAFlex'
  s.dependency 'mtopext'
  s.dependency 'FBRetainCycleDetector'
  s.dependency 'WeexAnalyzerBundle'
  s.dependency 'Masonry'
  s.dependency 'APPSecuritySDK'
  s.dependency 'LALocalization'
  s.dependency 'disguiser'
  s.dependency 'EscortService'
  s.dependency 'SDWebImage'

end

