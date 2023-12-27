import { Controller, Get, Param } from '@nestjs/common';
import { KeyWordService } from './key-word.service';

@Controller('key-word')
export class KeyWordController {
  constructor(private readonly keyWordService: KeyWordService) {}

  @Get()
  findAll() {
    return this.keyWordService.findAll();
  }

  @Get(':keyWord')
  findOne(@Param('keyWord') keyWord: string) {
    return this.keyWordService.findOne(keyWord);
  }
}
