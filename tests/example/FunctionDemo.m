//
//  FunctionDemo.m
//  Test
//
//  Created by luckytianyiyan on 16/8/6.
//  Copyright © 2016年 luckytianyiyan. All rights reserved.
//

#import "FunctionDemo.h"

@implementation FunctionDemo

- (instancetype)init
{
    if (self = [super init]) {
        LocalizedFunctionDemoString(@"Function.localizedString.function", @"Function.localizedString.function.commend");

        NSLocalizedString(@"Function.localizedString", @"Function.localizedString.commend");
    }
    return self;
}

static NSString * LocalizedFunctionDemoString(NSString *key, NSString *comment)
{
    return [[NSBundle mainBundle] localizedStringForKey:key value:key table:@"FunctionTable"];
}

@end
