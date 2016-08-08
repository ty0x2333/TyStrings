//
//  DefineDemo.m
//  Test
//
//  Created by luckytianyiyan on 16/8/6.
//  Copyright © 2016年 luckytianyiyan. All rights reserved.
//

#import "DefineDemo.h"

#define LOCALIZED(fmt, commend) NSLocalizedString(fmt, commend)
#define LOCALIZED_2 NSLocalizedString

@implementation DefineDemo

- (instancetype)init
{
    if (self = [super init]) {

        LOCALIZED(@"Define.localizedString.define", @"Define.localizedString.define.commend");
        LOCALIZED_2(@"Define.localizedString.define.2", @"Define.localizedString.define.2.commend");

        NSLocalizedString(@"Define.localizedString", @"Define.localizedString.commend");
    }
    return self;
}
@end
