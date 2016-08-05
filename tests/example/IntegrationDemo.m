//
//  integration.m
//  TyStringTest
//
//  Created by luckytianyiyan on 16/8/5.
//  Copyright © 2016年 luckytianyiyan. All rights reserved.
//

#import "integration.h"

@implementation IntegrationDemo

- (instancetype)init
{
    if (self = [super init]) {
        NSLocalizedString(@"integration.localized_string", @"integration.localized_string.commend");
        [[NSBundle mainBundle] localizedStringForKey:@"integration.localized_string_for_key" value:@"" table:nil];

        NSLocalizedStringFromTable(@"integration.localized_string_from_table", @"IntegrationTable", @"integration.localized_string_from_table.commend");
        [[NSBundle mainBundle] localizedStringForKey:@"integration.localized_string_from_table.oc" value:@"" table:@"IntegrationTable"];

        NSLocalizedStringWithDefaultValue(@"integration.localized_string_with_default_value", @"IntegrationTable", [NSBundle mainBundle], @"Integration.Value", @"integration.localized_string_with_default_value.commend");
        [[NSBundle mainBundle] localizedStringForKey:@"integration.localized_string_with_default_value.oc" value:@"integration.value" table:@"IntegrationTable"];
    }
    return self;
}

@end
