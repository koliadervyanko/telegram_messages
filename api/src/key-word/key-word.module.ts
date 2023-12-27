import { Module } from '@nestjs/common';
import { KeyWordService } from './key-word.service';
import { KeyWordController } from './key-word.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { KeyWordEntity } from './entities/key-word.entity';

@Module({
  controllers: [KeyWordController],
  providers: [KeyWordService],
  imports: [TypeOrmModule.forFeature([KeyWordEntity])],
  exports: [KeyWordService],
})
export class KeyWordModule {}
