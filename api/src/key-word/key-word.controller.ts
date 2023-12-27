import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { KeyWordService } from './key-word.service';
import { CreateKeyWordDto } from './dto/create-key-word.dto';

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

  @Post()
  create(@Body() createKeyWordDto: CreateKeyWordDto) {
    return this.keyWordService.create(createKeyWordDto);
  }
}
